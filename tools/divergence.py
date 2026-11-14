# -*- coding: utf-8 -*-
"""原始物分歧账（ADR-0045）：en/ 批准勘误的双账语义。

baseline/entries.json 的 files[].sha256 永远只记「原始网页 sha」（抓取时的上游
字节钉，ADR-0027/0038）；en/ 就地勘误（ADR-0038 四类）不得改写该钉，逐条登记
本账（baseline/divergences.json）：

  {slug, path, upstream_sha256, local_sha256, bytes, commit, subject,
   base_commit, reason, registered_at}

verify 门禁：任何 en/ 文件 sha ≠ 原始钉而未登记分歧 → 红灯（堵「静默改原文」）；
已登记而三账不符（钉被改、本地又被改）→ 同样红灯，须先搬运或修正账目。
上游真变时的搬运（逆向补丁，ADR-0045 决策 5）：carry 以 原始钉 为基做三方合并
（基→本地勘误 × 基→新上游；git merge-file 实现）——hunk 不相交自动随迁，相交出
冲突件转人工；随迁成功即归档新上游快照（results/upstream-snapshots/）、前移原始钉、
更新账目（base_snapshot 锚新原始字节）。patch 输出 原始字节→本地 的 unified diff。

子命令:
  verify [--deep]      三账一致性核验（--deep 加核锚点字节==原始钉：base_commit
                       的 git blob 或 base_snapshot 快照文件；浅克隆下 blob 不可核
                       如实报告，仅本地跑）
  register <path>...   登记批准分歧（--commit 勘误提交，缺省取该路径最新提交；
                       --reason 勘误定性说明）
  carry <path>         逆向补丁搬运：--new <新上游快照>；干净合并直接落盘并移钉；
                       冲突退出码 3 并出冲突件，人工解决后 --merged <文件> 复跑
  patch <path>         输出 原始→本地 unified diff（搬运用，diff 走 stdout）
  list                 概览
输出: JSON 走 stdout（patch 除外）；人读进度走 stderr。
退出码: 0 成功/全绿；1 有失败；2 用法/前置不满足；3 搬运冲突待人工。
"""
import argparse
import difflib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import (BASELINE_LOCK, load_json, repo_path, sha256_bytes,
                          sha256_file, utcnow_iso, write_json_verified)

# stdout 重包守卫：CI/unittest 下可能已是被别的模块重包过的流，重复包会关闭底层 buffer
if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DIV_PATH = ("baseline", "divergences.json")
SNAP_DIR = ("specs", "001-sep-sync-pipeline", "results", "upstream-snapshots")
SCHEMA = "sep-cn-divergences/1"


def load_divergences():
    path = repo_path(*DIV_PATH)
    if not os.path.exists(path):
        return {"schema": SCHEMA, "updated_at": None, "divergences": []}
    return load_json(path)


def save_divergences(div):
    div["schema"] = SCHEMA
    div["updated_at"] = utcnow_iso()
    with BASELINE_LOCK:
        write_json_verified(repo_path(*DIV_PATH), div)


def ledger_index():
    """baseline/entries.json → {path: {slug, sha256, bytes}}（kind=main 等 all）。"""
    path = repo_path("baseline", "entries.json")
    if not os.path.exists(path):
        return None
    base = load_json(path)
    idx = {}
    for r in base["entries"]:
        for f in r.get("files", []):
            idx[f["path"]] = {"slug": r["slug"], "sha256": f["sha256"],
                              "bytes": f.get("bytes")}
    return idx


def git_blob_sha(commit, path):
    """git show <commit>:<path> 的 sha256；取不到（浅克隆/坏提交）返回 None。"""
    r = subprocess.run(["git", "show", "%s:%s" % (commit, path)],
                       cwd=repo_path("."), capture_output=True)
    if r.returncode != 0:
        return None
    return sha256_bytes(r.stdout)


def find_base_commit(path, want_sha):
    """沿该路径的提交史从新到旧找原始字节所在提交（blob sha256 == 钉）。"""
    r = subprocess.run(["git", "log", "--format=%H", "--", path],
                       cwd=repo_path("."), capture_output=True, text=True)
    if r.returncode != 0:
        return None
    for c in r.stdout.split():
        if git_blob_sha(c, path) == want_sha:
            return c
    return None


def check_consistency(files_idx, divs, sha_of, deep=False, blob_sha=None,
                      snapshot_sha=None):
    """纯核验核心（可单测）：files_idx=台账索引，divs=分歧账列表，
    sha_of(path)->当前 sha 或 None（缺件），blob_sha(commit,path)->原始字节 sha 或
    None，snapshot_sha(path)->快照文件 sha 或 None。返回 (summary, failures)。"""
    failures = []
    pristine = divergent = 0
    div_map = {}
    for d in divs:
        p = d.get("path")
        if p in div_map:
            failures.append({"path": p, "reason": "分歧账重复登记"})
        div_map[p] = d
        if files_idx is not None and p not in files_idx:
            failures.append({"path": p, "reason": "分歧账路径不在 baseline/entries.json"})
    if files_idx is None:
        failures.append({"path": "baseline/entries.json", "reason": "台账缺失（先 fetch_entry）"})
        files_idx = {}
    for p, rec in files_idx.items():
        actual = sha_of(p)
        if actual is None:
            failures.append({"path": p, "slug": rec["slug"], "reason": "文件缺失"})
            continue
        if actual == rec["sha256"]:
            pristine += 1
            if p in div_map:
                failures.append({"path": p, "slug": rec["slug"],
                                 "reason": "文件与原始钉一致但分歧账仍有登记（账已过时，须清理）"})
            continue
        d = div_map.get(p)
        if d is None:
            failures.append({"path": p, "slug": rec["slug"],
                             "reason": "与原始钉不符且未登记分歧（静默改原文，ADR-0045 红灯）"})
            continue
        divergent += 1
        if d.get("upstream_sha256") != rec["sha256"]:
            failures.append({"path": p, "slug": rec["slug"],
                             "reason": "分歧账 upstream_sha256 与台账钉不符（钉已移动，搬运/修账未完成）"})
        if d.get("local_sha256") != actual:
            failures.append({"path": p, "slug": rec["slug"],
                             "reason": "分歧账 local_sha256 与现文件不符（登记后又改动）"})
        if not d.get("base_commit") and not d.get("base_snapshot"):
            failures.append({"path": p, "slug": rec["slug"],
                             "reason": "缺 base_commit/base_snapshot 锚点"})
        elif deep:
            if d.get("base_snapshot"):
                bs = snapshot_sha(d["base_snapshot"]) if snapshot_sha else None
                if bs is None:
                    failures.append({"path": p, "slug": rec["slug"],
                                     "reason": "base_snapshot 快照缺失，原始字节不可核"})
                elif bs != rec["sha256"]:
                    failures.append({"path": p, "slug": rec["slug"],
                                     "reason": "base_snapshot 快照 ≠ 原始钉（锚点有误）"})
            else:
                bs = blob_sha(d["base_commit"], p)
                if bs is None:
                    failures.append({"path": p, "slug": rec["slug"],
                                     "reason": "base_commit 原始字节不可核（浅克隆或历史缺失）"})
                elif bs != rec["sha256"]:
                    failures.append({"path": p, "slug": rec["slug"],
                                     "reason": "base_commit 的 blob ≠ 原始钉（登记证据有误）"})
    summary = {"checked": len(files_idx), "pristine": pristine,
               "divergent": divergent, "registered": len(divs),
               "failures": failures}
    return summary, failures


def cmd_verify(args):
    files_idx = ledger_index()
    div = load_divergences()
    summary, failures = check_consistency(
        files_idx, div.get("divergences", []),
        sha_of=lambda p: sha256_file(repo_path(p)) if os.path.exists(repo_path(p)) else None,
        deep=args.deep, blob_sha=git_blob_sha if args.deep else None)
    out = {"schema": SCHEMA, "at": utcnow_iso(), **summary}
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 1 if failures else 0


def cmd_register(args):
    files_idx = ledger_index()
    if files_idx is None:
        sys.stderr.write("[divergence] baseline/entries.json 缺失\n")
        return 2
    div = load_divergences()
    known = {d["path"] for d in div["divergences"]}
    added = []
    for p in args.paths:
        p = p.replace(os.sep, "/")
        rec = files_idx.get(p)
        if rec is None:
            sys.stderr.write("[divergence] %s 不在台账，先 fetch_entry\n" % p)
            return 2
        full = repo_path(p)
        if not os.path.exists(full):
            sys.stderr.write("[divergence] %s 文件缺失\n" % p)
            return 2
        actual = sha256_file(full)
        if actual == rec["sha256"]:
            sys.stderr.write("[divergence] %s 与原始钉一致，无需登记\n" % p)
            return 2
        if p in known:
            sys.stderr.write("[divergence] %s 已登记\n" % p)
            return 2
        commit = args.commit
        if commit:
            r = subprocess.run(["git", "log", "-1", "--format=%H%n%s", commit],
                               cwd=repo_path("."), capture_output=True, text=True)
            if r.returncode != 0:
                sys.stderr.write("[divergence] 提交 %s 不可解析\n" % commit)
                return 2
            subject = r.stdout.split("\n", 1)[1].strip()
        else:
            r = subprocess.run(["git", "log", "-1", "--format=%H%n%s", "--", p],
                               cwd=repo_path("."), capture_output=True, text=True)
            if r.returncode != 0 or not r.stdout.strip():
                sys.stderr.write("[divergence] %s 无提交史\n" % p)
                return 2
            commit, subject = r.stdout.strip().split("\n", 1)
        base = find_base_commit(p, rec["sha256"])
        if base is None:
            sys.stderr.write("[divergence] %s 在提交史中找不到原始字节（钉 %s…）\n"
                             % (p, rec["sha256"][:12]))
            return 2
        entry = {"slug": rec["slug"], "path": p,
                 "upstream_sha256": rec["sha256"], "local_sha256": actual,
                 "bytes": {"upstream": rec.get("bytes"), "local": os.path.getsize(full)},
                 "commit": commit, "subject": subject, "base_commit": base,
                 "reason": args.reason, "registered_at": utcnow_iso()}
        div["divergences"].append(entry)
        added.append(p)
        sys.stderr.write("[divergence] 登记 %s（勘误提交 %s，原始字节 %s）\n"
                         % (p, commit[:10], base[:10]))
    if added:
        save_divergences(div)
    print(json.dumps({"registered": added}, ensure_ascii=False, indent=1))
    return 0


def resolve_entry(p):
    div = load_divergences()
    for d in div["divergences"]:
        if d["path"] == p:
            return d
    return None


def cmd_patch(args):
    p = args.path.replace(os.sep, "/")
    d = resolve_entry(p)
    if d is None:
        sys.stderr.write("[divergence] %s 未登记分歧\n" % p)
        return 2
    r = subprocess.run(["git", "show", "%s:%s" % (d["base_commit"], p)],
                       cwd=repo_path("."), capture_output=True)
    if r.returncode != 0:
        sys.stderr.write("[divergence] 原始字节不可取（%s）\n" % d["base_commit"][:10])
        return 2
    old = r.stdout.decode("utf-8", "replace").splitlines()
    new = open(repo_path(p), "rb").read().decode("utf-8", "replace").splitlines()
    sys.stdout.writelines(difflib.unified_diff(
        old, new,
        fromfile="pristine:%s:%s" % (d["base_commit"][:10], p),
        tofile="local:%s" % p, lineterm=""))
    return 0


def cmd_list(args):
    div = load_divergences()
    print(json.dumps({"schema": SCHEMA, "updated_at": div.get("updated_at"),
                      "count": len(div["divergences"]),
                      "divergences": div["divergences"]},
                     ensure_ascii=False, indent=1))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("verify", help="三账一致性核验")
    v.add_argument("--deep", action="store_true",
                   help="加核 base_commit 的 git blob == 原始钉（需完整历史）")
    v.set_defaults(fn=cmd_verify)
    r = sub.add_parser("register", help="登记批准分歧")
    r.add_argument("paths", nargs="+", help="en/<slug>/<file> 路径")
    r.add_argument("--commit", help="勘误提交（缺省取该路径最新提交）")
    r.add_argument("--reason", help="勘误定性说明（ADR-0038 类别）")
    r.set_defaults(fn=cmd_register)
    p = sub.add_parser("patch", help="输出原始→本地 unified diff")
    p.add_argument("path")
    p.set_defaults(fn=cmd_patch)
    l = sub.add_parser("list", help="概览")
    l.set_defaults(fn=cmd_list)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())

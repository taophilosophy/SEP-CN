# -*- coding: utf-8 -*-
"""双机同步护栏（ADR-0028）：pull 判弃自检与积压自查。

用法:
  python tools/sync_guard.py pull     # fetch + rebase origin/main，拉后核对判弃
  python tools/sync_guard.py status   # 显示未推送提交（积压数），收工清零自查

pull 语义:
  拉前记录 origin/main..HEAD 本地提交清单，并以 git cherry 标注每件是否
  patch-identical（'-'，内容已在远程）。rebase 后逐条核对：
  * '-' 件被弃 → 放行，提示"判弃 N 件（内容已在远程）"；
  * '+' 件被弃 → 判弃事故，退出码 2，给 reflog 恢复指引；
  * rebase 停在冲突 → 退出码 3，人工解决或 abort。
status 语义:
  打印未推送提交数与清单；作业途中应 ≤1，收工时必须为 0。

退出码: 0 正常；2 非判弃性丢失（事故）；3 rebase 冲突待人工；4 git 异常/前置不满足。
"""
import io
import os
import subprocess
import sys
from collections import Counter


def _setup_stdout():
    """CLI 输出改 UTF-8。只在 main() 调用——导入期碰 sys.stdout 会踩
    discovery 链上前序模块包装器被 GC 关流留下的尸体（ValueError）。"""
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        try:
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        except (AttributeError, ValueError):
            pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXIT_OK, EXIT_LOST, EXIT_CONFLICT, EXIT_GIT = 0, 2, 3, 4


def git(*args):
    """跑 git 子命令；失败返回 (None, stderr)。"""
    r = subprocess.run(["git"] + list(args), capture_output=True, cwd=ROOT)
    if r.returncode != 0:
        return None, r.stderr.decode("utf-8", "replace").strip()
    return r.stdout.decode("utf-8", "replace"), None


def parse_oneline(text):
    """`git log --format=%H %s` 输出 → [(sha, subject), ...]（保序，最新在前）。"""
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        sha, _, subject = line.partition(" ")
        out.append((sha.strip(), subject))
    return out


def parse_cherry(text):
    """git cherry 输出 → {sha: flag}；flag '-'=patch-identical（内容已在远程）。"""
    flags = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        flag, _, sha = line.partition(" ")
        flags[sha.strip()] = flag
    return flags


def classify(pre, post):
    """比对 rebase 前后清单。

    pre: [(flag, sha, subject)]（flag 来自 git cherry）；
    post: [(sha, subject)]（rebase 后 origin/main..HEAD）。
    返回 (lost, dropped_eq, extra)：
      lost       = '+' 件被弃（事故，非 patch-identical）；
      dropped_eq = '-' 件被弃（内容已在远程，放行）；
      extra      = rebase 后多出的提交（异常情形，理论为空）。
    """
    remain = Counter(s for _, s in post)
    lost = []
    for flag, sha, subject in pre:
        if flag != "+":
            continue
        if remain[subject] > 0:
            remain[subject] -= 1
        else:
            lost.append((sha, subject))
    dropped_eq = [(sha, s) for flag, sha, s in pre if flag == "-"]
    extra = sorted(remain.elements())
    return lost, dropped_eq, extra


def rebase_in_progress():
    return os.path.isdir(os.path.join(ROOT, ".git", "rebase-merge")) or os.path.isdir(
        os.path.join(ROOT, ".git", "rebase-apply")
    )


def cmd_pull():
    out, err = git("fetch", "origin")
    if out is None:
        print(f"[sync_guard] fetch 失败：{err}")
        return EXIT_GIT

    pre_head, err = git("rev-parse", "HEAD")
    if pre_head is None:
        print(f"[sync_guard] rev-parse 失败：{err}")
        return EXIT_GIT
    pre_head = pre_head.strip()

    log, err = git("log", "--format=%H %s", "origin/main..HEAD")
    if log is None:
        print(f"[sync_guard] log 失败：{err}")
        return EXIT_GIT
    pre = [(sha, s) for sha, s in parse_oneline(log)]
    if not pre:
        print("[sync_guard] 本地无积压，直接 fast-forward。")
    cherry, err = git("cherry", "origin/main", "HEAD")
    if cherry is None:
        print(f"[sync_guard] cherry 失败：{err}")
        return EXIT_GIT
    flags = parse_cherry(cherry)
    pre_flagged = [(flags.get(sha, "+"), sha, s) for sha, s in pre]

    # git rebase origin/main == pull --rebase origin main（fetch 已做）
    _, err = git("rebase", "origin/main")
    if err is not None or rebase_in_progress():
        if rebase_in_progress():
            print(f"[sync_guard] rebase 停台（冲突）：{err or 'rebase 进行中'}")
            print("[sync_guard] 人工解决冲突后 git rebase --continue；放弃本次同步则 git rebase --abort。")
            return EXIT_CONFLICT
        print(f"[sync_guard] rebase 前置不满足：{err}")
        print("[sync_guard] 先提交或 stash 工作区改动再同步（本工具不做自动 stash）。")
        return EXIT_GIT

    log2, err = git("log", "--format=%H %s", "origin/main..HEAD")
    if log2 is None:
        print(f"[sync_guard] log 失败：{err}")
        return EXIT_GIT
    post = parse_oneline(log2)
    lost, dropped_eq, extra = classify(pre_flagged, post)

    if dropped_eq:
        print(f"[sync_guard] 判弃 {len(dropped_eq)} 件（patch-identical，内容已在远程）：")
        for sha, s in dropped_eq:
            print(f"  - {s}")
    if extra:
        print(f"[sync_guard] 注意：rebase 后多出 {len(extra)} 件：")
        for s in extra:
            print(f"  + {s}")
    if lost:
        print("[sync_guard] 事故：非 patch-identical 提交被判弃！")
        for sha, s in lost:
            print(f"  × {s}")
        print(f"[sync_guard] 恢复：先 git reflog 核对，确认后 git reset --hard {pre_head} "
              "回到 rebase 前，再按 rules/06 孤儿件处置上报，禁止静默。")
        return EXIT_LOST

    head, _ = git("rev-parse", "--short", "HEAD")
    print(f"[sync_guard] 同步完成：放行 {len(pre) - len(dropped_eq)} 件，HEAD={head.strip()}。")
    return EXIT_OK


def cmd_status():
    out, err = git("fetch", "origin")
    if out is None:
        print(f"[sync_guard] fetch 不可达（{err}），按本地 origin/main 引用计。")
    log, err = git("log", "--oneline", "origin/main..HEAD")
    if log is None:
        print(f"[sync_guard] log 失败：{err}")
        return EXIT_GIT
    items = parse_oneline(log)
    print(f"[sync_guard] 未推送提交 {len(items)} 件：")
    for _, s in items:
        print(f"  · {s}")
    if not items:
        print("[sync_guard] 收工判据满足：积压清零。")
    else:
        print("[sync_guard] 判据：作业途中 ≤1，收工时必须清零（ADR-0028）。")
    return EXIT_OK


def main(argv):
    _setup_stdout()
    if len(argv) != 2 or argv[1] not in ("pull", "status"):
        print(__doc__)
        return EXIT_GIT
    if argv[1] == "pull":
        return cmd_pull()
    return cmd_status()


if __name__ == "__main__":
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""把站点壳仓（taophilosophy.github.io）的 docs 指针前移到本仓最新提交并推送。

为什么需要它（ADR-0064）：`docs` 是壳仓里的 gitlink，**子模块指针不会自己变**——
SEP-CN 推多少次都不会动壳仓，因此站点不会自动更新。壳仓 `deploy.yml` 现在有三种
入口：`push`（只认 `docs` 指针变更）＝推送即部署；`schedule`（7,37）＝兜底轮询；
`workflow_dispatch`＝手动。本脚本负责第一条：推完 SEP-CN 顺手前移指针。

用法：
    python tools/deploy_bump.py                # 前移到 origin/main 并推送
    python tools/deploy_bump.py --gate         # 先跑 check_all.py，全绿才前移
    python tools/deploy_bump.py --dry-run      # 只报告将要做什么
    python tools/deploy_bump.py --no-push      # 只提交不推送（测试/离线用）
    python tools/deploy_bump.py --ref HEAD     # 前移到本地 HEAD 而非 origin/main
    python tools/deploy_bump.py --shell D:/x/taophilosophy.github.io

壳仓路径解析顺序：`--shell` → 环境变量 `SEP_SHELL_REPO` → 同级的
`taophilosophy.github.io/`。只提交 `docs` 一个路径，壳仓里的其它改动不碰。
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SHELL_NAME = 'taophilosophy.github.io'


def run(cmd: list[str], cwd: str, check: bool = True) -> subprocess.CompletedProcess:
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if check and r.returncode != 0:
        raise SystemExit('命令失败：%s\n%s%s' % (' '.join(cmd), r.stdout, r.stderr))
    return r


def git(cwd: str, *args: str, check: bool = True) -> str:
    r = run(['git', *args], cwd, check)
    return (r.stdout + '').strip()


def resolve_shell(arg: str | None) -> str:
    cand = arg or os.environ.get('SEP_SHELL_REPO') or os.path.join(os.path.dirname(ROOT), DEFAULT_SHELL_NAME)
    path = os.path.abspath(cand)
    if not os.path.isdir(os.path.join(path, '.git')) and not os.path.isfile(os.path.join(path, '.git')):
        raise SystemExit('找不到站点壳仓：%s（用 --shell 或 SEP_SHELL_REPO 指定）' % path)
    return path


def sep_sha(ref: str) -> tuple[str, str]:
    sha = git(ROOT, 'rev-parse', ref)
    subject = git(ROOT, 'log', '-1', '--format=%s', sha)
    return sha, subject


def docs_pointer(shell: str) -> str | None:
    """壳仓 HEAD 里记录的 docs gitlink；没有该条目时返回 None。"""
    out = git(shell, 'ls-tree', 'HEAD', '--', 'docs')
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 3 and parts[0] == '160000' and parts[3] == 'docs':
            return parts[2]
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description='前移壳仓 docs 指针并推送（ADR-0064）')
    ap.add_argument('--shell', help='壳仓路径（默认同级 taophilosophy.github.io）')
    ap.add_argument('--ref', default='origin/main', help='要把指针指到哪个 SEP-CN 提交（默认 origin/main）')
    ap.add_argument('--gate', action='store_true', help='先跑 tools/check_all.py，非全绿直接退出')
    ap.add_argument('--dry-run', action='store_true', help='只报告，不改动')
    ap.add_argument('--no-push', action='store_true', help='只提交不推送')
    ap.add_argument('--force', action='store_true', help='允许指针指向未在 origin/main 上的提交')
    ap.add_argument('--allow-dirty', action='store_true', help='允许壳仓有 docs 以外的未提交改动（仍只提交 docs）')
    args = ap.parse_args(argv)

    shell = resolve_shell(args.shell)

    if args.gate:
        print('[gate] python tools/check_all.py')
        r = run([sys.executable, os.path.join(ROOT, 'tools', 'check_all.py')], ROOT, check=False)
        tail = (r.stdout + r.stderr).strip().splitlines()[-1:] or ['']
        if r.returncode != 0:
            print('[gate] 门禁未全绿，拒绝前移指针（先修红项）：%s' % tail[0])
            return 1
        print('[gate] 全绿')

    target, subject = sep_sha(args.ref)
    # 指针必须指向**已推送**的提交，否则壳仓 CI 取不到对象（build 作业会红）
    pushed = git(ROOT, 'rev-parse', '--verify', '--quiet', 'origin/main', check=False)
    if pushed and not args.force and subprocess.run(
            ['git', 'merge-base', '--is-ancestor', target, 'origin/main'],
            cwd=ROOT, capture_output=True).returncode != 0:
        print('%s 不在 origin/main 上：先把 SEP-CN 推送（或改用 --ref origin/main）。'
              '确认要指向未推送提交可加 --force' % target[:9])
        return 1
    cur = docs_pointer(shell)
    print('壳仓：%s' % shell)
    print('目标：%s %s' % (target[:9], subject))
    print('当前指针：%s' % (cur[:9] if cur else '(无 docs 条目)'))
    if cur == target:
        print('指针已是最新，无需动作。')
        return 0

    # 壳仓必须能快进到 origin/main，避免把 bot 的指针提交落在落后分支上
    git(shell, 'fetch', 'origin', '--quiet', check=False)
    # 交给 git 做排除：porcelain 的 XY 前缀宽度不稳（子模块/重命名各有形态），
    # 自己切列会漏判；`:(exclude)docs` 只留 docs 以外的改动
    others = git(shell, 'status', '--porcelain', '--', '.', ':(exclude)docs')
    if others and not args.allow_dirty:
        print('壳仓有 docs 以外的未提交改动，拒绝提交（用 --allow-dirty 放行）：')
        for ln in others.splitlines()[:10]:
            print('  ' + ln)
        return 1
    def count(rng):
        # 壳仓可能没有 origin（离线克隆/测试夹具），此时按「不落后、不领先」处理
        out = git(shell, 'rev-list', '--count', rng, check=False)
        if not out.strip().isdigit():
            return 0
        return int(out.strip())

    ahead, behind = count('origin/main..HEAD'), count('HEAD..origin/main')
    if behind and not ahead:
        if args.dry_run:
            print('[dry-run] 会先 ff-only 到 origin/main（落后 %d 个提交）' % behind)
        else:
            git(shell, 'merge', '--ff-only', 'origin/main')
            print('壳仓已快进到 origin/main（%d 个提交）' % behind)
    elif ahead:
        print('壳仓有 %d 个未推送提交，请先处理（不自动 rebase，避免与并行会话抢）' % ahead)
        return 1

    brief = subject if len(subject) <= 60 else subject[:59] + '…'
    msg = 'docs 指针前移：%s %s' % (target[:9], brief)
    if args.dry_run:
        print('[dry-run] 将执行：git update-index --cacheinfo 160000,%s,docs && git commit -m %r%s' % (target, 
            msg, '' if args.no_push else ' && git push origin main'))
        return 0

    # 不用 `git add docs`：那记录的是**工作树里子模块当前 HEAD**，与 --ref 目标无关
    # （本地领先 origin/main 时会把未推送的提交写进指针，CI 取不到该对象）。
    # 直接按目标 sha 写索引，精确且与工作树状态无关。
    git(shell, 'update-index', '--add', '--cacheinfo', '160000,%s,docs' % target)
    if git(shell, 'diff', '--cached', '--name-only') != 'docs':
        print('暂存区异常（不止 docs），中止。')
        return 1
    git(shell, 'commit', '-m', msg)
    print('已提交：%s' % msg)
    if args.no_push:
        print('（--no-push：未推送，壳仓 push 事件未触发）')
        return 0
    git(shell, 'push', 'origin', 'main')
    print('已推送 → 壳仓 deploy.yml 的 push(paths: docs) 会立刻构建部署；'
          '进度：gh run list --workflow deploy.yml --limit 1')
    return 0


if __name__ == '__main__':
    sys.exit(main())

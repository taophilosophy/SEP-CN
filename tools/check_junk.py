# -*- coding: utf-8 -*-
"""垃圾入库门禁（ADR-0003 + ADR-0023）：扫描 git 跟踪清单与根目录工作区，命中即非零退出。

用法: python tools/check_junk.py
规则一（全库，跟踪清单）: 原始抓取物（en/）、运行时报告（.github/sep-sync-report/）、
      字节码缓存、构建产物（node_modules、.vitepress/cache|dist、.astro、.turbo、dist、coverage）、
      系统与编辑器杂物（.DS_Store、Thumbs.db、desktop.ini、*~、*.swp、*.tmp、*.bak、*.log）
      一律不得入库。可入库的事实源：baseline/、.github/sep-baseline/、PROGRESS.md（生成但受控）。
规则二（根目录白名单，ADR-0023）: 根目录只允许 ROOT_ALLOW 登记的条目（工具链配置、顶层叙事文档、
      A–Z 词条目录、结构目录、包管理文件）。跟踪清单与工作区（含被忽略物）双向核对——
      根级散件无论 `git add -A` 扫没扫到、忽略规则漏没漏，都算违规。
      会话散件归 `script/`（本地草稿）或 `state/`（运行态）；批次工件归
      `specs/<NNN>-*/bin|results/`（入库凭证）；新增根目录条目须走 ADR。
豁免: 无——命中即硬错误，由人工迁移/删除，必要时补忽略规则。
退出码: 0 无垃圾；1 命中。
"""
import io
import os
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATTERNS = [
    (r'(^|/)__pycache__/', 'Python 字节码缓存'),
    (r'\.(pyc|pyo)$', 'Python 字节码'),
    (r'\.log$', '日志'),
    (r'\.tmp$', '临时文件'),
    (r'\.bak$', '备份文件'),
    (r'\.swp$', '编辑器交换文件'),
    (r'~$', '编辑器备份'),
    (r'(^|/)\.DS_Store$', 'macOS 桌面杂物'),
    (r'(^|/)Thumbs\.db$', 'Windows 缩略图缓存'),
    (r'(^|/)desktop\.ini$', 'Windows 桌面配置'),
    (r'^node_modules/', 'Node 依赖（构建产物）'),
    (r'^\.vitepress/(cache|dist)/', 'VitePress 构建产物'),
    (r'^\.astro/', 'Astro 构建产物'),
    (r'^\.turbo/', 'Turbo 缓存'),
    (r'^dist/', '构建输出'),
    (r'^coverage/', '测试覆盖率输出'),
    (r'^\.(pytest_cache|mypy_cache|ruff_cache)/', '工具缓存'),
    (r'^en/', '原始抓取物（宪法 II / FR-014：仅存本地）'),
    (r'^\.github/sep-sync-report/', '同步检查运行时报告'),
    (r'^[^/]+\.html$', '根级 HTML 残留（站点页面误抓，仓库无合法根级 html；2026-10-27 audit 教训）'),
    (r'^_[^/]', '根级 `_` 前缀散件（会话脚手架不入库，批次工件归 specs/005/bin；2026-11-05 D24，add -A 扫入教训）'),
    (r'^tasks/[a-z]/_', '任务目录内 `_` 前缀散件（非 <slug>.json 命名约定；2026-11-05 D24）'),
]

# 根目录白名单（ADR-0023）：唯一允许出现在仓库根层的条目。新增项须走 rules/adr/。
ROOT_ALLOW = {
    # 工具链与配置（点前缀）
    '.git': '版本库本体',
    '.autocorrectrc': '拼写检查配置',
    '.gitattributes': 'Git 属性',
    '.gitignore': '忽略规则',
    '.markdownlint-cli2.jsonc': 'markdownlint 配置',
    '.github': 'CI 工作流与基线快照',
    '.vitepress': '本地双语阅读站',
    '.specify': '项目宪法与 spec-kit 脚手架',
    '.zcode': 'AI 代理配置',
    '.secrets': '本地凭证（忽略，不入库）',
    '.workbuddy': '本地工具态（忽略，不入库）',
    # 顶层叙事文档（单一事实源与访客文档）
    'AGENTS.md': 'AI 代理入口指引',
    'CODE_OF_CONDUCT.md': '行为准则',
    'CONTRIBUTING.md': '贡献指南',
    'LICENSE': '许可',
    'README.md': '访客说明',
    'RELEASE-NOTES.md': '发布说明',
    'PROGRESS.md': '进度汇总（受控生成物）',
    'SUMMARY.md': '目录结构唯一数据源',
    'mu-lu-s.md': '手工分类目录',
    'yi-zhe-shuo-ming.md': '术语与人名登记册',
    'ren-ming-biao.md': '人名对照表',
    # 结构目录
    'assets': '词条图片（正文 ../assets/ 引用）',
    'baseline': '版本钉基线',
    'en': '原始抓取 HTML（忽略，仅存本地）',
    'fang-fa-lun': '翻译工程方法论散页',
    'guan-yu': '项目说明页',
    'jian-yi-shu': '一次性交付物',
    'node_modules': 'Node 依赖（忽略，可重建）',
    'public': '站点静态资产',
    'qian-yan': '项目说明页',
    'rules': '全局规则与 ADR',
    'script': '本地草稿脚本区（忽略，会话自理）',
    'specs': '工程规格与执行记录',
    'state': '管线本地运行态（忽略）',
    'tasks': '任务状态记录',
    'tools': '管线与治理脚本',
    'yuanwen': '英文原文镜像（忽略，仅存本地）',
    # 包管理
    'package.json': '站点依赖声明',
    'bun.lock': 'bun 锁文件',
}
# A–Z 词条字母目录 + 个别非字母目录（ADR-0009：digit 开头 slug 归 `1/`）
ROOT_ALLOW.update({c: '词条字母目录' for c in 'abcdefghijklmnopqrstuvwxyz'})
ROOT_ALLOW['1'] = '非字母词条目录（digit slug）'

ROOT_FIX_HINT = ('根目录只放白名单条目；散件迁 script/（本地）或 specs/<NNN>-*/bin|results/（入库），'
                 '临时文件写 state/')


def tracked_files():
    out = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT,
                         capture_output=True, check=True).stdout
    return [p.decode('utf-8') for p in out.split(b'\0') if p]


def root_hits(tracked, root_dir=None):
    """根层白名单核对：跟踪清单（入库存量）与工作区（新增散件）双向。"""
    root_dir = root_dir or ROOT
    hits = []
    tracked_tops = {p.split('/')[0] for p in tracked}
    for top in sorted(tracked_tops - set(ROOT_ALLOW)):
        is_dir = os.path.isdir(os.path.join(root_dir, top))
        hits.append((top + ('/' if is_dir else ''),
                     '根目录未登记目录（已入库）' if is_dir else '根目录散件（已入库）'))
    for name in sorted(os.listdir(root_dir)):
        if name in ROOT_ALLOW:
            continue
        kind = '根目录未登记目录（工作区）' if os.path.isdir(os.path.join(root_dir, name)) else '根目录散件（工作区）'
        hits.append((name, kind))
    return hits


def main():
    tracked = tracked_files()
    hits = [(path, why) for path in tracked for pat, why in PATTERNS if re.search(pat, path)]
    root = root_hits(tracked)
    if hits or root:
        if hits:
            print('垃圾/产物入库：%d 个文件（退出码 1，需 git rm --cached 并补忽略）' % len(hits))
            for path, why in hits[:50]:
                print('  %s  <-  %s' % (path, why))
            if len(hits) > 50:
                print('  … 其余 %d 个略' % (len(hits) - 50))
        if root:
            print('根目录白名单：%d 项越界（退出码 1）' % len(root))
            for name, why in root[:50]:
                print('  %s  <-  %s' % (name, why))
            print('  ' + ROOT_FIX_HINT)
        return 1
    print('垃圾/产物入库检查：0 命中（跟踪文件 %d 个；根目录 %d 项全在白名单）'
          % (len(tracked), len(os.listdir(ROOT))))
    return 0


if __name__ == '__main__':
    sys.exit(main())

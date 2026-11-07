# -*- coding: utf-8 -*-
"""图片引用检查（rules/01「图片」三条硬性要求；CI check-images 工作流的数据源）。

检查项：
  1. 悬空引用 —— md 引用的本地图片文件不存在；
  2. 大小写不符 —— 仅大小写不同的文件存在（Windows 不敏感、Linux CI 404）；
  3. 未本地化 —— 引用 http(s)/data 等外部地址；
  4. 未引用资产 —— `assets/**` 下的图片文件无任何 md 引用（rules/01：每个图片文件至少被引用一次）。

口径：
  * 只扫 md（跳过代码块与行内代码里的字面量，如文档示例 `<img src="imageN.jpg">`）；
  * `yuanwen/**` 不入库：CI 无该目录时凡指向 `yuanwen/` 的引用跳过并计数（ADR-0010 镜像桥），
    本地有该目录时照常解析；
  * 只报告，不改内容；退出码 0（问题经报告落地，CI 由 check-images 工作流开 issue）。

用法：
    python tools/check_images.py                  # 报告写 state/image-report.md（本地，不入库）
    python tools/check_images.py --out image-report.md   # CI 工作流用法（仓库根）
"""
import argparse
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') if (
    getattr(sys.stdout, 'encoding', '').lower().replace('-', '') != 'utf8'
    and hasattr(sys.stdout, 'buffer')) else sys.stdout
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {'.git', '.gitbook', 'node_modules', 'script', 'state', '.zcode',
             '.vitepress', 'public', 'dist', 'en', 'yuanwen'}
MD_IMG = re.compile(r'!\[(?:[^\[\]]|\[[^\[\]]*\])*\]\(\s*([^)\s]+)')
HTML_IMG = re.compile(r'<img[^>]*\bsrc=["\']([^"\']+)["\']', re.I)
# 图片文件作为链接目标（如 `[![](small.gif)](large.gif)` 的点击放大）；
# 同一行的两种写法可能重复命中，scan() 按（文件, 引用）去重。
LINK_IMG = re.compile(r'\]\(\s*([^)\s]+\.(?:png|jpe?g|gif|svg|webp|bmp))(?:\s|\))', re.I)
REMOTE = re.compile(r'^(https?:|data:|mailto:|ftp:|//)', re.I)
INLINE_CODE = re.compile(r'`[^`]*`')
IMG_EXT = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp')


def iter_refs(text):
    """逐行产出（引用, 种类）；种类 img/html=嵌入图片，link=图片文件作链接目标。

    跳过围栏代码块与行内代码（文档示例里的 `<img src="imageN.jpg">` 不算引用）。
    """
    fence = False
    for line in text.split('\n'):
        s = line.strip()
        if s.startswith('```') or s.startswith('~~~'):
            fence = not fence
            continue
        if fence:
            continue
        s = INLINE_CODE.sub('', line)
        for m in MD_IMG.finditer(s):
            yield m.group(1), 'img'
        for m in HTML_IMG.finditer(s):
            yield m.group(1), 'html'
        for m in LINK_IMG.finditer(s):
            yield m.group(1), 'link'


def resolve(md_path, ref):
    target = os.path.normpath(os.path.join(os.path.dirname(md_path), ref.split('#')[0]))
    return target


def exact_exists(target):
    """文件存在且文件名大小写逐字符一致（Windows 的 isfile 大小写不敏感，会掩盖 CI 404）。"""
    if not os.path.isfile(target):
        return False
    d, base = os.path.split(target)
    try:
        return base in os.listdir(d)
    except OSError:
        return False


def case_hit(target):
    d, base = os.path.split(target)
    if not os.path.isdir(d):
        return None
    for cand in os.listdir(d):
        if cand.lower() == base.lower():
            return os.path.join(d, cand)
    return None


def scan(root):
    dangling, case_bad, remote, readable = [], [], [], 0
    referenced = set()
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in filenames:
            if fn.endswith('.md'):
                md_files.append(os.path.join(dirpath, fn))
    for path in md_files:
        rel = os.path.relpath(path, root).replace(os.sep, '/')
        try:
            with open(path, encoding='utf-8-sig') as f:
                text = f.read()
        except (OSError, UnicodeDecodeError):
            continue
        seen = set()
        for ref, kind in iter_refs(text):
            if ref in seen:
                continue
            seen.add(ref)
            if kind == 'link':
                # 图片文件作链接目标（放大图 / 译注里的外部图片链接）：
                # 外部地址不属图片本地化范畴（外链检查归 links.yml），只核本地存在性
                if REMOTE.match(ref) or ref.startswith('#'):
                    continue
            elif REMOTE.match(ref) or ref.startswith('#'):
                remote.append((rel, ref))
                continue
            target = resolve(path, ref)
            if exact_exists(target):
                readable += 1
                referenced.add(os.path.abspath(target))
                continue
            rel_target = os.path.relpath(target, root).replace(os.sep, '/')
            if rel_target.startswith('yuanwen/assets/') \
                    and not os.path.isdir(os.path.join(root, 'yuanwen', 'assets')):
                continue  # 镜像资产未随仓（CI 检出只有 yuanwen 的少量跟踪文件），跳过
            hit = case_hit(target)
            if hit:
                case_bad.append((rel, ref, os.path.relpath(hit, root).replace(os.sep, '/')))
            else:
                dangling.append((rel, ref))
    # 未引用资产
    assets_dir = os.path.join(root, 'assets')
    orphans = []
    for dirpath, dirnames, filenames in os.walk(assets_dir):
        for fn in filenames:
            if not fn.lower().endswith(IMG_EXT):
                continue
            full = os.path.join(dirpath, fn)
            if os.path.abspath(full) not in referenced:
                orphans.append(os.path.relpath(full, root).replace(os.sep, '/'))
    return {
        'md_files': len(md_files), 'readable': readable,
        'dangling': dangling, 'case': case_bad, 'remote': remote,
        'orphans': sorted(orphans),
    }


def render(res):
    out = ['# 图片检查报告', '']
    out.append('扫描 md %d 个；可解析本地引用 %d 条；悬空 %d、大小写不符 %d、外部地址 %d、未引用资产 %d。'
               % (res['md_files'], res['readable'], len(res['dangling']),
                  len(res['case']), len(res['remote']), len(res['orphans'])))
    out.append('')
    if res['dangling']:
        out += ['## 悬空引用（引用的图片文件不存在）', '', '| 词条 | 引用 |', '| ---- | ---- |']
        out += ['| %s | `%s` |' % (a, b) for a, b in res['dangling']]
        out.append('')
    if res['case']:
        out += ['## 大小写不符（Linux CI 会 404）', '', '| 词条 | 引用 | 实际文件 |', '| ---- | ---- | ---- |']
        out += ['| %s | `%s` | `%s` |' % (a, b, c) for a, b, c in res['case']]
        out.append('')
    if res['remote']:
        out += ['## 未本地化（外部地址）', '', '| 词条 | 引用 |', '| ---- | ---- |']
        out += ['| %s | `%s` |' % (a, b) for a, b in res['remote']]
        out.append('')
    if res['orphans']:
        out += ['## 未引用资产（`assets/` 下无任何引用的图片）', '']
        out += ['* `%s`' % p for p in res['orphans']]
        out.append('')
    return '\n'.join(out).rstrip() + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='图片引用检查（rules/01 图片三条硬性要求）')
    ap.add_argument('--root', default=ROOT)
    ap.add_argument('--out', default=os.path.join(ROOT, 'state', 'image-report.md'),
                    help='报告输出路径（无问题时删除旧报告）')
    args = ap.parse_args(argv)

    res = scan(args.root)
    total = len(res['dangling']) + len(res['case']) + len(res['remote']) + len(res['orphans'])
    print('图片引用检查：md %d | 可解析 %d | 悬空 %d | 大小写 %d | 外链 %d | 未引用资产 %d'
          % (res['md_files'], res['readable'], len(res['dangling']), len(res['case']),
             len(res['remote']), len(res['orphans'])))
    if total:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, 'w', encoding='utf-8', newline='') as f:
            f.write(render(res))
        print('报告：%s' % args.out)
    else:
        if os.path.isfile(args.out):
            os.remove(args.out)
        print('OK：图片引用无问题')
    return 0


if __name__ == '__main__':
    sys.exit(main())

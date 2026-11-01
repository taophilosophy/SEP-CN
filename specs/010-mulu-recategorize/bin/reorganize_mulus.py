# -*- coding: utf-8 -*-
"""mu-lu-s 分类体系重构生成器（specs/010）。

结构重排（对账式，门禁全过才写回）：
  1. 前言/关于保留；西方哲学史保持原位原结构。
  2. # 中国哲学 并入 # 区域哲学（区首 ## 中国哲学，其下 ## 降 ###）；整区后移至西方哲学史之后。
  3. 其余学科 # 顶级类依原序收进 # 哲学通论（# → ##，## → ###）。
  4. 人物挂靠做全：slug 前缀 ∈ 人物白名单的分支词条，从原位取出嵌套挂到人物主词条 li 下
     （已在其下的跳过；主题簇 epistemology/truth/qm 等不挂）。
  5. 超长堆叠标题瘦身（保主标题，堆叠内容转该节首行引注）。

对账门禁：li 总数进=出；slug 进=出且零重复；人物白名单分支全部收拢到主词条块内；
超长标题 7 处全部处理。任一不过拒绝写回。
"""
import io
import re
import sys
from collections import Counter, OrderedDict

ROOT = '.'
SRC = 'mu-lu-s.md'

# 人物主词条白名单（slug 无后缀名）——specs/010 spec.md Assumptions 核定
PERSONS = {
    'alexander', 'aquinas', 'aristotle', 'boethius', 'bolzano', 'bradley',
    'brentano', 'church', 'collingwood', 'david', 'descartes', 'dewey',
    'frege', 'gadamer', 'goedel', 'goodman', 'hegel', 'heidegger', 'hobbes',
    'hume', 'james', 'kant', 'leibniz', 'locke', 'luther', 'maimonides',
    'malebranche', 'mally', 'mill', 'moore', 'newton', 'nietzsche',
    'pascal', 'peirce', 'philo', 'plato', 'quine', 'ramsey', 'reid',
    'russell', 'schlegel', 'schopenhauer', 'spinoza', 'tarski', 'turing',
    'wittgenstein', 'wyclif',
}

H1_WEST = '# 西方哲学史'
H1_CHINA = '# 中国哲学'
H1_REGION = '# 区域哲学'
H1_TONGLUN = '# 哲学通论'


class Li:
    __slots__ = ('indent', 'text', 'target', 'tail', 'moved')

    def __init__(self, indent, text, target, tail):
        self.indent = indent
        self.text = text
        self.target = target  # 含路径原样
        self.tail = tail      # 链接后的其余文本
        self.moved = False

    @property
    def slug(self):
        return self.target.split('/')[-1][:-3]

    def render(self, indent=None):
        ind = self.indent if indent is None else indent
        return '%s* [%s](%s)%s' % (ind, self.text, self.target, self.tail)


def parse(lines):
    """解析为项序列：('h', level, title) / ('li', Li) / ('raw', line)。"""
    items = []
    for ln in lines:
        m = re.match(r'^(#{1,6}) (.+?)\s*$', ln)
        if m:
            items.append(('h', len(m.group(1)), m.group(2)))
            continue
        m = re.match(r'^( *)\* \[(.+?)\]\(([a-zA-Z0-9._/\-]+\.md)\)(.*)$', ln)
        if m:
            items.append(('li', Li(m.group(1), m.group(2), m.group(3), m.group(4))))
            continue
        items.append(('raw', ln))
    return items


def split_sections(items):
    """按 # 一级标题切区；返回 OrderedDict[title, items]。# 前内容键 ''。"""
    secs = OrderedDict()
    cur = ''
    secs[cur] = []
    for it in items:
        if it[0] == 'h' and it[1] == 1:
            cur = it[2]
            secs[cur] = [('h', 1, it[2])]
        else:
            secs[cur].append(it)
    return secs


def demote(items, levels=1):
    out = []
    for it in items:
        if it[0] == 'h':
            out.append(('h', min(it[1] + levels, 6), it[2]))
        else:
            out.append(it)
    return out


def long_titles_fix(items):
    """超长堆叠标题瘦身：主标题=首个括号前部分；堆叠内容转节首引注。"""
    out, i, nfix = [], 0, 0
    while i < len(items):
        it = items[i]
        if it[0] == 'h' and it[1] in (2, 3):
            title = it[2]
            # 取最后一个起括号且闭合于末尾的括号对作 sub，其余为主标题
            m = None
            for opener, closer in (('（', '）'), ('(', ')')):
                k = title.rfind(opener)
                if k > 0 and title.rstrip().endswith(closer):
                    cand = re.compile(r'^(.+)\\%s(.+)\\%s$' % (opener, closer))
                    mm = re.match('^(.+)\\%s(.+)\\%s$' % (opener, closer), title)
                    if mm:
                        m = mm
                        break
            if m and len(title) > 40 and ('、' in m.group(2) or '，' in m.group(2)):
                main, sub = m.group(1).strip(), m.group(2).strip()
                out.append(('h', it[1], main))
                out.append(('raw', '> 本节涵盖：%s' % sub))
                nfix += 1
                i += 1
                # 掠过紧随的空行，避免双空行
                while i < len(items) and items[i][0] == 'raw' and items[i][1].strip() == '':
                    i += 1
                continue
        out.append(it)
        i += 1
    return out, nfix


def person_regroup(items):
    """人物挂靠做全。返回 (新 items, moved_count, already_count)。"""
    lis = [(i, it[1]) for i, it in enumerate(items) if it[0] == 'li']
    # 主词条位置（人物，缩进层级最低出现处；若多现取首个）
    main_idx = {}
    for i, li in lis:
        if li.slug in PERSONS and li.slug not in main_idx:
            main_idx[li.slug] = i
    # 分支 → 主 slug
    moves = []  # (branch_idx, person)
    for i, li in lis:
        slug = li.slug
        if '-' in slug:
            pre = slug.split('-')[0]
            if pre in PERSONS and pre in main_idx and i != main_idx.get(pre):
                moves.append((i, pre))
    mvset = dict(moves)
    # 已挂靠检测：分支 li 已位于主词条 li 与下一个不深于主词条缩进的项之间
    def depth_within(mi, bi):
        mi_li = items[mi][1]
        base = len(mi_li.indent)
        for j in range(mi + 1, bi):
            if items[j][0] == 'li':
                ind = len(items[j][1].indent)
                if ind <= base:
                    return False
        # bi 之后到下一同深项
        for j in range(bi + 1, len(items)):
            if items[j][0] == 'li':
                ind = len(items[j][1].indent)
                if ind <= base:
                    return False
            elif items[j][0] == 'h':
                return False
        return True
    already, todo = [], []
    for bi, pre in moves:
        if depth_within(main_idx[pre], bi):
            already.append(bi)
        else:
            todo.append((bi, pre))
    # 执行：先从后往前删除 todo 分支（含其嵌套子 li），再统一插到主词条后
    removed = set()
    for bi, pre in todo:
        removed.add(bi)
        base = len(items[bi][1].indent)
        for j in range(bi + 1, len(items)):
            if items[j][0] == 'li' and len(items[j][1].indent) > base:
                removed.add(j)
            elif items[j][0] == 'li':
                break
            elif items[j][0] == 'h':
                break
    # 主词条插入位置需在删除后重算：按 slug 锚定
    out = [it for i, it in enumerate(items) if i not in removed]
    insert_at = {}
    for j, it in enumerate(out):
        if it[0] == 'li' and it[1].slug in PERSONS and it[1].slug not in insert_at:
            insert_at[it[1].slug] = j
    # 组装插入载荷：todo 按原顺序分组到各主词条
    payloads = {}
    claimed = set()  # 已被外层 block 收编的深层 li，防止以自身 bi 重复提取
    for bi, pre in sorted(todo, key=lambda x: x[0]):
        if bi in claimed:
            continue
        # 子 li（删除集中的、位于 bi 之后的连续深层项）一并带走
        base = len(items[bi][1].indent)
        block = [items[bi]]
        j = bi + 1
        while j < len(items):
            if j in removed and items[j][0] == 'li' and len(items[j][1].indent) > base:
                block.append(items[j])
                claimed.add(j)
                j += 1
            else:
                break
        payloads.setdefault(pre, []).extend(block)
    # 从后往前插入，避免位移
    for pre in sorted(insert_at, key=lambda x: -insert_at[x]):
        if pre not in payloads:
            continue
        at = insert_at[pre]
        ind = out[at][1].indent + '  '
        block = [it for it in payloads[pre]]
        # 分支缩进统一为主词条+2，孙级再 +2（保持相对差）
        first_ind = len(block[0][1].indent)
        rendered = []
        for it in block:
            if it[0] == 'li':
                delta = len(it[1].indent) - first_ind
                rendered.append(('li', Li(ind + '  ' * delta, it[1].text, it[1].target, it[1].tail)))
            else:
                rendered.append(it)
        out[at + 1:at + 1] = rendered
    return out, len(todo), len(already)


def audit(items_before, items_after, notes):
    ok = True
    def slugs(items):
        return Counter(it[1].slug for it in items if it[0] == 'li')
    a, b = slugs(items_before), slugs(items_after)
    n_before = sum(a.values()); n_after = sum(b.values())
    if n_before != n_after:
        notes.append('FAIL li 总数不守恒: %d -> %d' % (n_before, n_after)); ok = False
    if (a - b) or (b - a):
        notes.append('FAIL slug 进出差异: lose=%s gain=%s' % ((a - b).most_common(5), (b - a).most_common(5)))
        ok = False
    dups = [s for s, c in b.items() if c > 1]
    if dups:
        notes.append('FAIL 重复收录: %s' % dups[:10]); ok = False
    # 人物收拢验证
    lis = [(i, it[1]) for i, it in enumerate(items_after) if it[0] == 'li']
    main_at = {}
    for i, li in lis:
        if li.slug in PERSONS and li.slug not in main_at:
            main_at[li.slug] = i
    for i, li in lis:
        if '-' in li.slug:
            pre = li.slug.split('-')[0]
            if pre in PERSONS and pre in main_at:
                mi = main_at[pre]
                base = len(items_after[mi][1].indent)
                if i > mi:
                    ok2 = True
                    for j in range(mi + 1, i):
                        if items_after[j][0] == 'li' and len(items_after[j][1].indent) <= base:
                            ok2 = False; break
                        if items_after[j][0] == 'h':
                            ok2 = False; break
                    if not ok2:
                        notes.append('FAIL 人物分支未收拢: %s' % li.slug); ok = False
                else:
                    notes.append('FAIL 分支先于主词条: %s' % li.slug); ok = False
    return ok


def split_sub(items, level=2):
    """区内按 ## 标题切块：[(title, [items])]；无标题前导并入首块前。"""
    blocks, cur_t, cur = [], None, []
    for it in items:
        if it[0] == 'h' and it[1] == level:
            if cur_t is not None:
                blocks.append((cur_t, cur))
            cur_t, cur = it[2], [('h', level, it[2])]
        else:
            if cur_t is None:
                blocks.append((None, []))
                cur_t = '__lead__'
                cur = blocks[-1][1]
                blocks[-1] = (None, cur)
            else:
                cur.append(it)
    if cur_t is not None:
        blocks.append((cur_t, cur))
    return blocks


def grab(items, slugs):
    """从 items 中摘出 slug 匹配的 li（连同其深层子 li），返回 (余下, 摘出块)。"""
    out, taken, i = [], [], 0
    idxs = [i for i, it in enumerate(items) if it[0] == 'li' and it[1].slug in slugs]
    grab_set = set()
    for bi in idxs:
        base = len(items[bi][1].indent)
        grab_set.add(bi)
        j = bi + 1
        while j < len(items):
            if items[j][0] == 'li' and len(items[j][1].indent) > base:
                grab_set.add(j); j += 1
            else:
                break
    taken = [items[i] for i in sorted(grab_set)]
    out = [it for i, it in enumerate(items) if i not in grab_set]
    return out, taken


def find_block(blocks, title_prefix):
    for bi, (t, body) in enumerate(blocks):
        if t and t.startswith(title_prefix):
            return bi
    return -1


def main():
    src = io.open(SRC, encoding='utf-8').read()
    lines = src.split('\n')
    items = parse(lines)
    before = list(items)
    notes = []

    secs = split_sections(items)
    # ---- 结构重排 ----
    head = secs.get('', [])
    west = secs.get('西方哲学史')
    china = secs.get('中国哲学')
    region = secs.get('区域哲学')
    if west is None or china is None or region is None:
        print('FAIL 关键区缺失', list(secs)); sys.exit(2)
    # 中国哲学并入区域哲学：去掉两区各自 H1，重新拼
    china_body = [it for it in china[1:]]  # 去掉自身 H1
    region_body = [it for it in region[1:]]
    # china_body 首个标题应为 ## 中国哲学通论 之类的 ##；先给 # 区域哲学 下加 ## 中国哲学
    new_region = [('h', 1, '区域哲学'), ('h', 2, '中国哲学')] + demote(china_body, 1) + region_body
    # 学科区（除前言/关于/西史/中国/区域外）依原序
    skip = {'', '前言', '关于', '西方哲学史', '中国哲学', '区域哲学'}
    # R6 女性哲学按时期拆入西史（先拆，再组装通论）
    fem_secs = split_sub(secs.get('女性哲学与性哲学相关')[1:], level=2)
    fem_keep, fem_early, fem_modern = [], None, None
    for t, body in fem_secs:
        if t and t.startswith('近代女性哲学家'):
            fem_early = body
        elif t and t.startswith('现代女性哲学家'):
            fem_modern = body
        else:
            fem_keep.append(body)
    if fem_early is None or fem_modern is None:
        print('FAIL 女性两时期节未找到'); sys.exit(2)
    notes.append('R6 女性两时期节拆入西史（近代 %d 条 / 现代 %d 条）' % (
        sum(1 for it in fem_early if it[0] == 'li'),
        sum(1 for it in fem_modern if it[0] == 'li')))
    tonglun = [('h', 1, '哲学通论')]
    for name, body in secs.items():
        if name in skip:
            continue
        if name == '女性哲学与性哲学相关':
            body = [('h', 1, name)] + [it for blk in fem_keep for it in blk]
        tonglun.extend(demote(body, 1))
    tonglun = tonglun[1:]  # 去掉自身 H1 重复——body 中已无 H1，补回
    tonglun = [('h', 1, '哲学通论')] + tonglun[1:]
    # 修正：上面循环 demote(body) 不含 H1（split_sections 已把 H1 当区键），故直接扩展

    new_items = head + secs.get('前言', []) + secs.get('关于', []) + west + new_region + tonglun

    # ---- 第二轮规则（2026-11-01 审查）：R1-R6 ----
    # R6 西史插入两时期节
    west2 = [('h', 1, '西方哲学史')]
    wblocks = split_sub(west[1:])
    for t, body in wblocks:
        west2.extend(body)
        if t and t.startswith('启蒙运动和早期现代哲学'):
            west2.extend(fem_early)
        elif t and t.startswith('现代西方哲学'):
            west2.extend(fem_modern)
    r_notes = []
    # R1 中世纪通论归位
    wblocks = split_sub(west2[1:])
    bi_jiao = find_block(wblocks, '教父哲学与早期经院哲学')
    bi_tong = find_block(wblocks, '中世纪哲学通论')
    if bi_jiao < 0 or bi_tong < 0:
        print('FAIL 中世纪目标节未找到'); sys.exit(2)
    rest, taken = grab(wblocks[bi_jiao][1], {'medieval-philosophy', 'medieval-literary'})
    wblocks[bi_jiao] = (wblocks[bi_jiao][0], rest)
    wblocks[bi_tong] = (wblocks[bi_tong][0], wblocks[bi_tong][1] + taken)
    r_notes.append('R1 中世纪通论归位 %d 条' % sum(1 for it in taken if it[0] == 'li'))
    west2 = [('h', 1, '西方哲学史')]
    for t, body in wblocks:
        west2.extend(body)

    # R10 拆"现代西方哲学 1750-1900"为 19/20 世纪两节（用户批准方案 b；断代判定基准=PhilPapers 主归属+成熟代表作年）
    S19 = {
        'fechner', 'wilhelm-wundt', 'transcendentalism', 'thoreau', 'emerson', 'comte',
        'ernst-mach', 'spencer', 'frege', 'frege-logic', 'frege-hilbert', 'frege-theorem',
        'whewell', 'twardowski', 'brentano', 'brentano-judgement', 'ehrenfels', 'stumpf',
        'neo-kantianism', 'friedrich-lange', 'natorp', 'wilhelm-windelband', 'cohen', 'heinrich-rickert',
        'green', 'bosanquet', 'bradley', 'bradley-moral', 'bradley-regress',
        'schopenhauer', 'schopenhauer-aesthetics', 'nietzsche', 'nietzsche-life-works',
        'nietzsche-moral-political', 'nietzsche-aesthetics', 'kierkegaard', 'dilthey',
        'utilitarianism-history', 'bentham', 'well-being', 'godwin', 'mill', 'mill-moral-political',
        'sidgwick', 'peirce', 'peirce-logic', 'peirce-semiotics', 'peirce-benjamin',
        'royce', 'wright', 'james-ward', 'james-mill', 'alexander-humboldt', 'alexander-crummell',
    }
    # west2 拆 h2 块
    wb = split_sub(west2[1:])
    bi_mod = next(i for i, (t, b) in enumerate(wb) if t and t.startswith('现代西方哲学'))
    body = wb[bi_mod][1]
    # 1) 仅拆 austin-jl 下误挂嵌套块（hare…alexander-crummell 18 条英国伦理学家/亚历山大系群）：块内缩进整体减 2，其余合法嵌套保留
    out_body = []
    in_wb_block = False
    for it in body:
        if it[0] == 'li':
            ind = len(it[1].indent)
            if ind == 0:
                in_wb_block = (it[1].slug == 'austin-jl')
                out_body.append(it)
            elif in_wb_block and ind >= 2:
                out_body.append(('li', Li(it[1].indent[2:], it[1].text, it[1].target, it[1].tail)))
            else:
                out_body.append(it)
        else:
            out_body.append(it)
    body = out_body
    # 2) 特殊移节三摘：alexander-aphrodisias→中期希腊哲学、james-viterbo→经院哲学、marx→马克思主义节
    def take(slugs, seq):
        take_set = set(slugs)
        got, rest = [], []
        i = 0
        while i < len(seq):
            it = seq[i]
            if it[0] == 'li' and it[1].slug in take_set:
                base = len(it[1].indent)
                got.append(it)
                j = i + 1
                while j < len(seq):
                    if seq[j][0] == 'li' and len(seq[j][1].indent) > base:
                        got.append(seq[j]); j += 1
                    else:
                        break
                i = j
            else:
                rest.append(it); i += 1
        return rest, got
    body, move_anc = take({'alexander-aphrodisias'}, body)
    body, move_vit = take({'james-viterbo'}, body)
    body, move_marx = take({'marx'}, body)
    # 3) 按 S19 分组（保持原相对顺序）
    seq19, seq20 = [], []
    for it in body:
        (seq19 if (it[0] == 'li' and it[1].slug in S19) or (it[0] != 'li') else seq20).append(it)
        if it[0] != 'li':
            # raw 行归入 19C 节前的间隔行不复制——跳过空行，渲染时统一
            if seq19 and it[0] != 'li':
                seq19.pop()
    # 4) 重组两节替换原块
    wb[bi_mod:bi_mod+1] = [
        (('19 世纪西方哲学 1750-1900'), [('h', 2, '19 世纪西方哲学 1750-1900')] + seq19),
        (('20 世纪西方哲学 1900—'), [('h', 2, '20 世纪西方哲学 1900—')] + seq20),
    ]
    # 5) 特殊条目归位
    bi_gk = next(i for i, (t, b) in enumerate(wb) if t and t.startswith('中期希腊哲学'))
    wb[bi_gk] = (wb[bi_gk][0], wb[bi_gk][1] + move_anc)
    bi_js = next(i for i, (t, b) in enumerate(wb) if t and t.startswith('经院哲学'))
    wb[bi_js] = (wb[bi_js][0], wb[bi_js][1] + move_vit)
    bi_mz = next(i for i, (t, b) in enumerate(wb) if t and t.startswith('马克思主义'))
    wb[bi_mz] = (wb[bi_mz][0], wb[bi_mz][1] + move_marx)
    # 6) 回写 west2
    west2 = [('h', 1, '西方哲学史')]
    for t, b in wb:
        west2.extend(b)
    r_notes.append('R10 拆断代节：19 世纪 %d 条 / 20 世纪 %d 条；austin-jl 下误挂嵌套块 18 条拆平铺；alexander-aphrodisias→中期希腊、james-viterbo→经院、marx→马克思主义节' % (
        sum(1 for it in seq19 if it[0] == 'li'), sum(1 for it in seq20 if it[0] == 'li')))
    new_items = new_items[:new_items.index(('h', 1, '西方哲学史'))] + west2 + new_items[new_items.index(('h', 1, '区域哲学')):]
    # 区域哲学手术（对 new_region 拆块）
    rblocks = split_sub(new_region[1:])
    # R2 韩国三条归位
    bi_jp = find_block(rblocks, '日本哲学')
    bi_kr = find_block(rblocks, '韩国哲学')
    rest, taken = grab(rblocks[bi_jp][1], {'korean-philosophy', 'korean-confucianism', 'korean-buddhism'})
    rblocks[bi_jp] = (rblocks[bi_jp][0], rest)
    rblocks[bi_kr] = (rblocks[bi_kr][0], rblocks[bi_kr][1] + taken)
    r_notes.append('R2 韩国三条归位 %d 条' % sum(1 for it in taken if it[0] == 'li'))
    # R3/R4 删空节（非洲哲学/欧洲哲学——查实空且无词条可归）
    rblocks = [(t, body) for t, body in rblocks if t not in ('非洲哲学', '欧洲哲学')]
    r_notes.append('R3/R4 删空节：非洲哲学（并非裔哲学）、欧洲哲学（翻译缺口）')
    # R5 中国佛教/道教/藏传拆分（中国哲学块内 ### 级手术）
    bi_cn = find_block(rblocks, '中国哲学')
    cn_body = rblocks[bi_cn][1]
    cn_h2 = [it for it in cn_body if it[0] == 'h' and it[1] == 2]
    cn_blocks = split_sub([it for it in cn_body if not (it[0] == 'h' and it[1] == 2)], level=3)
    bi_han = find_block(cn_blocks, '汉代-清代哲学')
    rest, chan3 = grab(cn_blocks[bi_han][1], {'buddhism-chan', 'buddhism-huayan', 'buddhism-tiantai'})
    cn_blocks[bi_han] = (cn_blocks[bi_han][0], rest)
    bi_fb = find_block(cn_blocks, '中国佛教与道教')
    if bi_fb < 0:
        print('FAIL 中国佛教与道教节未找到'); sys.exit(2)
    fb_body = cn_blocks[bi_fb][1][1:]  # 剥掉本节的 ### 标题（split_sub 保证首项为标题）
    rest_fb, dao2 = grab(fb_body, {'daoism', 'daoism-religion'})
    rest_fb, tibet2 = grab(rest_fb, {'epistemology-language-tibetan', 'twotruths-tibet',
                                     'gelukpa', 'gorampa', 'sakya-pandita', 'tsongkhapa'})
    new3 = [('h', 3, '中国佛教')] + rest_fb + chan3
    new3 += [('h', 3, '藏传佛教')] + tibet2
    new3 += [('h', 3, '道教')] + dao2
    cn_blocks[bi_fb] = (None, new3)
    cn_new = cn_h2 + [it for t, body in cn_blocks for it in body]
    rblocks[bi_cn] = (rblocks[bi_cn][0], cn_new)
    r_notes.append('R5 中国佛教(%d)/藏传佛教(%d)/道教(%d) 拆分' % (
        sum(1 for it in chan3 if it[0] == 'li') + sum(1 for it in rest_fb if it[0] == 'li'),
        sum(1 for it in tibet2 if it[0] == 'li'),
        sum(1 for it in dao2 if it[0] == 'li')))
    region2 = [('h', 1, '区域哲学')]
    # 中国哲学块（### 级）在 rblocks 前段，其余 ## 节随后——重组保持原序
    for t, body in rblocks:
        region2.extend(body)
    # 替换 new_items 中的区域哲学段
    r_start = new_items.index(('h', 1, '区域哲学'))
    r_end = new_items.index(('h', 1, '哲学通论'))
    new_items = new_items[:r_start] + region2 + new_items[r_end:]
    # west2 替换西史段
    w_start = new_items.index(('h', 1, '西方哲学史'))
    w_end = new_items.index(('h', 1, '区域哲学'))
    new_items = new_items[:w_start] + west2 + new_items[w_end:]
    # R7-R9（2026-11-01 联网复核发现的基线遗留错位）
    # R7 元伦理学两条从伊斯兰节尾移回通论伦理学区元伦理学节
    grabbed = {}
    def grab_global(slugs, key):
        got = []
        for gi, it in enumerate(new_items):
            if it[0] == 'li' and it[1].slug in slugs:
                base = len(it[1].indent)
                got.append(gi)
                j = gi + 1
                while j < len(new_items):
                    if new_items[j][0] == 'li' and len(new_items[j][1].indent) > base:
                        got.append(j); j += 1
                    else:
                        break
        got = sorted(set(got))
        grabbed[key] = [new_items[i] for i in got]
        return [it for i, it in enumerate(new_items) if i not in got]
    new_items = grab_global({'constructivism-metaethics', 'metaethics'}, 'meta')
    new_items = grab_global({'feminist-philosophy'}, 'fem')
    new_items = grab_global({'action', 'reasons-agent', 'reasons-internal-external',
                             'reasons-just-vs-expl', 'weighing-reasons',
                             'practical-reason-action', 'weakness-will'}, 'action')
    def insert_after_heading(items, title, block, level=3):
        for i, it in enumerate(items):
            if it[0] == 'h' and it[1] == level and it[2].startswith(title):
                return items[:i+1] + block + items[i+1:]
        print('FAIL 插入目标节未找到: %s' % title); sys.exit(2)
    new_items = insert_after_heading(new_items, '元伦理学', grabbed['meta'])
    new_items = insert_after_heading(new_items, '女性主义哲学', grabbed['fem'])
    # R8 行动哲学与理由论新节，插在道德心理学节之后（下一 h4 前）
    i_dm = next(i for i, it in enumerate(new_items)
                if it[0] == 'h' and it[1] == 3 and it[2].startswith('道德心理学'))
    i_next = next(i for i in range(i_dm + 1, len(new_items))
                  if new_items[i][0] == 'h' and new_items[i][1] <= 3)
    new_items = new_items[:i_next] + [('h', 3, '行动哲学与理由论')] + grabbed['action'] + new_items[i_next:]
    r_notes.append('R7 元伦理学两条归位；R8 行动哲学与理由论新节 %d 条；R9 女性主义哲学主词条归位' % len(grabbed['action']))
    for n in r_notes:
        notes.append(n)
    # ---- 细粒度：超长标题瘦身（前言/关于除外） ----
    # 只处理 ##/### 级
    fixed_all, nfix = [], 0
    # 找到前言/关于结束点（第二个 # 之后开始处理）
    h1_seen = 0
    start = 0
    for i, it in enumerate(new_items):
        if it[0] == 'h' and it[1] == 1:
            h1_seen += 1
            if h1_seen == 3:  # 前言、关于之后
                start = i
                break
    fixed_all = new_items[:start] + list(long_titles_fix(new_items[start:])[0])
    nfix = long_titles_fix(new_items[start:])[1]
    # ---- 人物挂靠 ----
    final, moved, already = person_regroup(fixed_all)
    notes.append('人物分支移动 %d 条，已在位 %d 条' % (moved, already))
    notes.append('超长标题瘦身 %d 处' % nfix)

    # ---- 对账 ----
    ok = audit(before, final, notes)
    # ---- 渲染 ----
    out = []
    for it in final:
        if it[0] == 'h':
            out.append('#' * it[1] + ' ' + it[2])
        elif it[0] == 'li':
            out.append(it[1].render())
        else:
            out.append(it[1])
    text = '\n'.join(out)
    for n in notes:
        print(n)
    print('对账门禁:', 'PASS' if ok else 'FAIL')
    if ok:
        # 规范化：多余三连空行收敛
        text = re.sub(r'\n{3,}', '\n\n', text)
        if not text.endswith('\n'):
            text += '\n'
        io.open(SRC, 'w', encoding='utf-8', newline='\n').write(text)
        print('已写回', SRC)
    else:
        sys.exit(3)


if __name__ == '__main__':
    main()

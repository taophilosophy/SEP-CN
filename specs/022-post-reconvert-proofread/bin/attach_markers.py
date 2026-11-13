# -*- coding: utf-8 -*-
r"""022 主引擎：标记偿还——把重转后 yuanwen 已挂而译文未挂的 [^key] 补挂到 zh 引文组后。

用法:
  python -I specs/022/bin/attach_markers.py <slug>...            # 试算：只出计划不写回
  python -I specs/022/bin/attach_markers.py <slug>... --apply    # 写回 + 应用日志
  python -I specs/022/bin/attach_markers.py --from-queue N M     # 按 triage 队列取 slug

语义与防线（rules/05 批量改写纪律）:
  - 只处理 done 词条（在途件 zh 由账本 compose 重生成，直改必冲突——记台账移交）。
  - 锚定：yw 标记前引文组的 (姓, 年) 对在 zh 对应组内计分匹配；≥60% 且唯一才挂，
    否则记 manual（人工判读）。
  - 前置门：key 必须已有 zh defs（[^key]:），缺 def 记 no-def 不挂（缺件另案）。
  - 幂等：只挂 only_yw 键；重跑零改动。逐条留 evidence；写回后自动复扫差额。
"""
import io
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
MARKER = re.compile(r'\[\^([^\]\s]+)\](?!:)')
DEF = re.compile(r'^\[\^([^\]\s]+)\]:', re.M)
CJK = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')
# 引文组内的 (姓[, et al.]…, 年) 候选
PAIR = re.compile(
    r"([A-ZÀ-ÖØ-Þ][\w\u00C0-\u024F'\u2019\u02BC\-]*)(?:[,\s]+(?:et\.?\s*al\.?|and|&|等)\b)?[^();，；]{0,50}?(?:[,，]\s*)?(\d{4})")
GROUP = re.compile(r'[（(][^（）()]*[）)]')
DEF_LINE = re.compile(r'^\[\^(%s)\]:')


def read(p):
    with io.open(p, encoding='utf-8', newline='') as f:
        return f.read()


def write(p, t):
    with io.open(p, 'w', encoding='utf-8', newline='') as f:
        f.write(t)


def pairs_of(group_text):
    """组内 (姓, 年) 对，归一小写。"""
    out = set()
    for m in PAIR.finditer(group_text):
        out.add((m.group(1).lower().replace('\u2019', "'").replace('\u02BC', "'"),
                 m.group(2)))
    return out


def zh_spans(zh):
    """zh 中候选引文组 span 列表（全角/半角括号）。"""
    spans = []
    for m in GROUP.finditer(zh):
        spans.append((m.start(), m.end()))
    return spans


def body_cut(zh):
    """zh 正文截止位：第一个文献/工具类 H2 标题处（defs 照录区不参与 span 候选）。"""
    m = re.search(r'^##\s*(参考文献|References|Bibliography|学术工具|Academic Tools)', zh, re.M)
    return m.start() if m else len(zh)


def plan_entry(slug, letter):
    zh_p = os.path.join(ROOT, letter, slug + '.md')
    yw_p = os.path.join(ROOT, 'yuanwen', letter, slug + '.md')
    zh, yw = read(zh_p), read(yw_p)
    mk_zh = Counter(m.group(1) for m in MARKER.finditer(zh))
    mk_yw = Counter(m.group(1) for m in MARKER.finditer(yw))
    defs_zh = set(DEF.findall(zh))
    debt = mk_yw - mk_zh
    plan, manual = [], []
    cut = body_cut(zh)
    spans = [(a, b) for (a, b) in zh_spans(zh[:cut])]
    used_spans = set()    # 已处理的 zh span（位点级）
    deficit = {k: mk_yw[k] - mk_zh[k] for k in debt}
    planned_count = {k: 0 for k in debt}
    # 按 yw 出现序聚类 run（相邻标记 ≤1 字符间隔 = 同一引文组链）
    occ = list(MARKER.finditer(yw))
    runs, cur = [], []
    for om in occ:
        if cur and om.start() - cur[-1].end() <= 1:
            cur.append(om)
        else:
            if cur:
                runs.append(cur)
            cur = [om]
    if cur:
        runs.append(cur)
    for run in runs:
        todo = []
        for om in run:
            k = om.group(1)
            if k in deficit and deficit[k] > planned_count[k]:
                todo.append(k)
        if not todo:
            continue
        if any(k not in defs_zh for k in todo):
            for k in todo:
                if k not in defs_zh:
                    manual.append({'key': k, 'reason': 'no-def'})
                    planned_count[k] += 1  # 记为已处置（manual）
            continue
        ctx = yw[max(0, run[0].start() - 420):run[0].start()]
        groups = list(GROUP.finditer(ctx))
        g = groups[-1] if groups else None
        pairs = pairs_of(g.group(0)) if g else set()
        if not pairs:
            manual.append({'key': ','.join(todo), 'reason': 'no-group', 'ctx': ctx[-90:]})
            for k in todo:
                planned_count[k] += 1
            continue
        scored = []
        for (a, b) in spans:
            text = zh[a:b]
            got = sum(1 for (s, y) in pairs if s in text.lower() and y in text)
            if got > 0:
                scored.append((got, a, b))
        if not scored:
            manual.append({'key': ','.join(todo), 'reason': 'no-zh-group',
                           'group': (g.group(0)[:80] if g else '')})
            for k in todo:
                planned_count[k] += 1
            continue
        scored.sort(key=lambda x: (-x[0], x[1]))
        top = scored[0][0]
        cands = [(a, b) for sc, a, b in scored if sc == top]
        need = max(1, int(round(len(pairs) * 0.6)))
        if top < need:
            manual.append({'key': ','.join(todo), 'reason': 'weak-match',
                           'score': top, 'need': need})
            for k in todo:
                planned_count[k] += 1
            continue
        pick = None
        for ab in cands:
            if ab not in used_spans:
                pick = ab
                break
        if pick is None:
            manual.append({'key': ','.join(todo), 'reason': 'ambiguous',
                           'cands': len(cands), 'ctx': ctx[-70:]})
            for k in todo:
                planned_count[k] += 1
            continue
        a, b = pick
        used_spans.add(pick)
        # 位点级已付检查：该组后已有同键标记者跳过
        window = zh[b:b + 140]
        todo = [k for k in todo if ('[^' + k + ']') not in window]
        for k in todo:
            plan.append({'key': k, 'at': b,
                         'evidence': zh[max(0, a - 30):min(b + 10, a + 90)],
                         'score': top, 'group_size': len(pairs)})
            planned_count[k] += 1
    ins = {}
    for p in plan:
        ins.setdefault(p['at'], []).append(p)
    return {'slug': slug, 'letter': letter, 'zh_p': zh_p,
            'debt': dict(debt), 'plan': plan, 'inserts': ins, 'manual': manual,
            'mk_zh': sum(mk_zh.values()), 'mk_yw': sum(mk_yw.values())}


def apply_plan(pl):
    zh = read(pl['zh_p'])
    # 从后往前插，防偏移；同一位置多键按 yw 顺序
    edits = sorted(pl['inserts'].items(), key=lambda x: -x[0])
    applied = []
    for at, items in edits:
        seq = ''.join('[^%s]' % it['key'] for it in items)
        # 幂等守卫：目标点之后若已是同串则跳过
        if zh[at:at + len(seq)] == seq:
            continue
        zh = zh[:at] + seq + zh[at:]
        applied.append({'at': at, 'keys': [it['key'] for it in items],
                        'evidence': zh[max(0, at - 60):at]})
    write(pl['zh_p'], zh)
    return applied


def main(argv):
    apply = '--apply' in argv
    args = [a for a in argv if not a.startswith('--')]
    slugs = list(args)
    out_log = os.path.join(ROOT, 'specs', '022-post-reconvert-proofread', 'results',
                           'attach-log.jsonl')
    done_letters = {}
    for letter in sorted(os.listdir(ROOT)):
        if len(letter) == 1 and letter.isalpha() and os.path.isdir(os.path.join(ROOT, letter)):
            for fn in os.listdir(os.path.join(ROOT, letter)):
                if fn.endswith('.md'):
                    done_letters[fn[:-3]] = letter
    if slugs and slugs[0] == '--queue':
        pass
    results = []
    for slug in slugs:
        letter = done_letters.get(slug)
        if not letter:
            print('SKIP no-doc %s' % slug)
            continue
        # done 门禁：tasks/<L>/<slug>.json state==done
        tj = os.path.join(ROOT, 'tasks', letter, slug + '.json')
        state = None
        if os.path.exists(tj):
            try:
                state = json.load(io.open(tj, encoding='utf-8')).get('state')
            except Exception:
                state = 'parse-error'
        if state != 'done':
            print('SKIP not-done %s (state=%s)' % (slug, state))
            continue
        pl = plan_entry(slug, letter)
        n_plan = len(pl['plan'])
        n_manual = len(pl['manual'])
        if apply and n_plan:
            applied = apply_plan(pl)
        else:
            applied = []
        # 复扫
        zh2 = read(pl['zh_p'])
        mk2 = Counter(m.group(1) for m in MARKER.finditer(zh2))
        yw2 = Counter(m.group(1) for m in MARKER.finditer(
            read(os.path.join(ROOT, 'yuanwen', letter, slug + '.md'))))
        remain = sum((yw2 - mk2).values())
        rec = {'slug': slug, 'letter': letter, 'state': state,
               'debt_keys': len(pl['debt']), 'planned': n_plan,
               'applied': len(applied), 'manual': n_manual,
               'only_yw_after': remain,
               'manual_detail': pl['manual'][:12]}
        results.append(rec)
        with io.open(out_log, 'a', encoding='utf-8') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        print('%-28s debt=%-4d planned=%-4d applied=%-4d manual=%-3d remain_yw=%d' %
              (slug, rec['debt_keys'], rec['planned'], rec['applied'],
               rec['manual'], remain))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

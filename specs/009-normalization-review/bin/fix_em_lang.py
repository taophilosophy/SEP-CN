# -*- coding: utf-8 -*-
"""fix_em_lang.py — T-em-lang-drop 修复生成器 v2（计数对账法）。

对每个 (文件, 术语) 对：
  en 侧 lang-em 出现次数 == yw 侧未包裹词界出现次数 → 全部补插 '*'
  计数不等 → fail-closed 报告人工处置。
门1 全量对账；门2 残余归零（写后复扫=0）；门3 幂等（重跑 0 变更）。
用法：python fix_em_lang.py [--write]
"""
import io, re, os, sys, glob, html
from collections import defaultdict

DRY = '--write' not in sys.argv

EM_LANG = re.compile(r'<em\s+lang="[^"]*"[^>]*>(.*?)</em\s*>', re.S)
TAG = re.compile(r'<[^>]+>')
WORD = 'A-Za-zÀ-ÿĀ-žḀ-ỿḈḍḌḍḤḥĶķḷḶṂṃṆṇṚṛṢṣṬṭŪūẒẓ'


def decode_term(inner):
    """em 内内容 → 解码纯文本术语。"""
    s = TAG.sub('', inner)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def build_term_counts():
    """扫描全部 en 包 → {(yp_path, term): count}。"""
    counts = {}
    pages = []
    for d in sorted(glob.glob('en/*/')):
        slug = d.replace('\\', '/').rstrip('/').split('/')[1]
        letter = slug[0]
        for hp in sorted(glob.glob(d + '*.html')):
            name = os.path.basename(hp)[:-5]
            if name in ('index', 'notes'):
                yp = 'yuanwen/%s/%s.md' % (letter, slug)
            else:
                yp = 'yuanwen/%s/%s.%s.md' % (letter, slug, name)
            pages.append((slug, name, hp, yp))

    for slug, name, hp, yp in pages:
        raw = io.open(hp, encoding='utf-8', errors='replace').read()
        for m in EM_LANG.finditer(raw):
            term = decode_term(m.group(1))
            if term:
                key = (yp, term)
                counts[key] = counts.get(key, 0) + 1
    return counts, pages


def yw_count(text, term):
    """yw 中词界未包裹出现次数。"""
    pat = re.compile(r'(?<![' + WORD + r'*])(?:' + re.escape(term) + r')(?![' + WORD + r'*])')
    n = 0
    for m in pat.finditer(text):
        pre = text[m.start() - 1] if m.start() > 0 else ''
        post = text[m.end()] if m.end() < len(text) else ''
        if pre == '*' and post == '*':
            continue  # 已包裹
        if (text[m.start()-2:m.start()] == '**' and text[m.end():m.end()+2] == '**'):
            continue  # 已加粗
        n += 1
    return n

def yw_count_orig(text, term):
    pat = re.compile(r'(?<![' + WORD + r'])(?' + re.escape(term) + r')(?![' + WORD + r'])')
    return len(pat.findall(text))


def in_italic_span(text, s, e):
    """[s,e) 是否落在既有 '*...*' 行内斜体跨度内（≤200 字符且不含换行）。"""
    if s > 0 and text[s - 1] == '*':
        o = s - 1
    else:
        o = text.rfind('*', 0, s)
        if o == -1:
            return False
    if e < len(text) and text[e] == '*':
        c = e
    else:
        c = text.find('*', e)
        if c == -1:
            return False
    if c - o > 200 or '\n' in text[o:c]:
        return False
    return o < s and c > e


DEFERRED_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             '..', 'results', 'para-review', 'em-lang-deferred.txt')


def load_frozen():
    """已冻结的挂起 (yp, term) 集：一旦挂起永不复评（幂等关键）。"""
    frozen = set()
    if os.path.exists(DEFERRED_PATH):
        with io.open(DEFERRED_PATH, encoding='utf-8') as f:
            for line in f:
                parts = line.rstrip('\n').split('\t')
                if len(parts) >= 2 and not line.startswith('T-em-lang'):
                    frozen.add((parts[0], parts[1]))
    return frozen


def main():
    en_counts, pages = build_term_counts()
    frozen = load_frozen()

    # 按目标文件分组
    by_file = defaultdict(list)
    for (yp, term), cnt in en_counts.items():
        by_file[yp].append((term, cnt))

    total_en = sum(en_counts.values())
    total_already = 0
    total_wrap = 0
    mismatches = []
    deferred = set(frozen)  # 冻结项并入挂起集：门2 同样豁免
    per_file = {}

    for yp in sorted(by_file.keys()):
        if not os.path.exists(yp):
            for term, cnt in by_file[yp]:
                deferred.add((yp, term))
                mismatches.append((yp, term, cnt, 'TARGET-MISSING'))
            continue
        text = io.open(yp, encoding='utf-8').read()
        wraps = []  # (start, end)——本文件全部待插区间
        file_already = 0
        for term, en_cnt in sorted(by_file[yp], key=lambda x: -len(x[0])):  # 长术语优先
            if (yp, term) in frozen:
                continue  # 冻结挂起项：永不复评（幂等关键）
            pat = re.compile(r'(?<![' + WORD + r'])(?:' + re.escape(term) + r')(?![' + WORD + r'])')
            free = []
            n_span = 0
            n_star = 0
            term_bad = False
            for m in pat.finditer(text):
                s, e = m.start(), m.end()
                pre = text[s - 1] if s > 0 else ''
                post = text[e] if e < len(text) else ''
                if pre == '*' and post == '*':
                    n_star += 1  # 已精确斜体（译文原有或本生成器先前轮次所补）
                    continue
                if text[max(0, s - 2):s] == '**' and text[e:e + 2] == '**':
                    n_star += 1
                    continue
                if any(s < we and ws < e for ws, we in wraps):
                    continue  # 与更长术语的待插区间真相交（同起点前缀/同终点后缀/内部）→ 覆盖
                if in_italic_span(text, s, e):
                    n_span += 1  # 短语斜体内已视觉斜体，参与对账但不再包裹
                    continue
                if pre == '*' or post == '*':
                    term_bad = True
                    break
                free.append((s, e))
            if term_bad:
                deferred.add((yp, term))
                mismatches.append((yp, term, en_cnt, 'ADJ-ASTERISK'))
                continue  # 仅该术语挂起，同文件其余术语照常
            file_already += n_star
            if n_star >= en_cnt:
                continue  # 视觉覆盖已足额 → 满足，不再动（幂等关键）
            deficit = en_cnt - n_star
            if not (len(free) <= deficit <= len(free) + n_span):
                deferred.add((yp, term))
                mismatches.append((yp, term, en_cnt,
                                   'COUNT-MISMATCH yw_free=%d in_span=%d starred=%d' % (len(free), n_span, n_star)))
                continue
            wraps.extend(free)
        # 应用插入（位置降序）
        new = text
        for rs, re_ in sorted(wraps, key=lambda x: -x[0]):
            new = new[:rs] + '*' + new[rs:re_] + '*' + new[re_:]
        # 门：只插入验证（升序撤销还原旧文）
        chk = new
        verify_ok = True
        for rs, re_ in sorted(wraps, key=lambda x: x[0]):
            if not (chk[rs] == '*' and chk[re_ + 1] == '*'):
                mismatches.append((yp, '(file)', 0, 'INSERT-VERIFY'))
                verify_ok = False
                break
            chk = chk[:rs] + chk[rs + 1:re_ + 1] + chk[re_ + 2:]
        if not verify_ok:
            continue
        if chk != text:
            mismatches.append((yp, '(file)', 0, 'INSERT-RESIDUE'))
            continue
        per_file[yp] = (len(by_file[yp]), file_already, len(wraps))
        total_already += file_already
        total_wrap += len(wraps)
        if not DRY and wraps:
            io.open(yp, 'w', encoding='utf-8', newline='').write(new)

    # 门2 残余归零：写后全量复扫（视觉斜体覆盖 = *term* 字面包裹 + 短语斜体内命中；挂起项豁免）
    if not DRY:
        residual = 0
        en_counts2, _ = build_term_counts()
        for (yp, term), en_cnt in sorted(en_counts2.items()):
            if not os.path.exists(yp) or (yp, term) in deferred:
                continue
            text = io.open(yp, encoding='utf-8').read()
            pat = re.compile(r'(?<![' + WORD + r'])(?:' + re.escape(term) + r')(?![' + WORD + r'])')
            covered = 0
            for m in pat.finditer(text):
                if m.group(0) != term:
                    continue
                s, e = m.start(), m.end()
                pre = text[s - 1] if s > 0 else ''
                post = text[e] if e < len(text) else ''
                if (pre == '*' and post == '*') or \
                   (text[max(0, s - 2):s] == '**' and text[e:e + 2] == '**') or \
                   in_italic_span(text, s, e):
                    covered += 1
            if covered < en_cnt:
                residual += en_cnt - covered
                print('  残余: %s %r en=%d covered=%d' % (yp, term[:40], en_cnt, covered))
        print('门2 残余（非挂起项中 en 有斜体而 yw 视觉未覆盖）:', residual)
        if residual:
            print('FAIL: 残余未归零')
            sys.exit(1)

    print('en lang-em 总数: %d | 已带斜体: %d | 本次补插: %d | 挂起术语: %d' % (total_en, total_already, total_wrap, len(deferred)))
    print('改动文件数:', len(per_file))
    for yp in sorted(per_file):
        n, a, w = per_file[yp]
        print('  %-42s terms=%-3d already=%-3d wrap=%d' % (yp, n, a, w))
    if mismatches:
        print('--- 计数不匹配（fail-closed，需人工）---')
        from collections import Counter
        cc = Counter(m[3].split(' ')[0] for m in mismatches)
        for k, v in cc.most_common():
            print('  %s: %d' % (k, v))
        for m in mismatches[:30]:
            print('  %s %r en=%d %s' % m)
        if len(mismatches) > 30:
            print('  ...共', len(mismatches))
    # 挂起清单持久化（无论干跑/落盘）
    dpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '..', 'results', 'para-review', 'em-lang-deferred.txt')
    with io.open(dpath, 'w', encoding='utf-8') as f:
        f.write('T-em-lang-drop 挂起术语清单（fail-closed，待人工逐处锚定） %d 项\n' % len(deferred))
        for yp, term in sorted(deferred):
            f.write('%s\t%s\t en=%d\n' % (yp, term, en_counts.get((yp, term), 0)))
    print('挂起清单已写入', os.path.normpath(dpath))
    if DRY:
        print('DRY RUN — 加 --write 落盘')
    else:
        print('WROTE')

if __name__ == '__main__':
    main()

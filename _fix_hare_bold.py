import re

path = 'h/hare.md'
text = open(path, encoding='utf-8').read()
lines = text.split('\n')

BEFORE_PUNCT = "（“‘【《—…，。、；：？！）】》”’"
AFTER_PUNCT = "，。、；：？！）】》”’…—（《,.!?)]}"
EMPH_RE = re.compile(r"\*\*[^*\n]+\*\*")

fixed = 0
newlines = []
for line in lines:
    if '`' in line:
        parts = line.split('`')
        segs = [(parts[i], i % 2 == 1) for i in range(len(parts))]
    else:
        segs = [(line, False)]
    rebuilt = []
    for seg, iscode in segs:
        if iscode or not seg:
            rebuilt.append(seg)
            continue
        # find all bold spans with positions, then insert spaces right-to-left
        spans = list(EMPH_RE.finditer(seg))
        # rebuild by walking forward, inserting spaces as needed
        out = []
        pos = 0
        for m in spans:
            start, end = m.start(), m.end()
            before = seg[start - 1] if start > 0 else ""
            after = seg[end] if end < len(seg) else ""
            ins_before = ""
            ins_after = ""
            if before and before not in " \t" and before not in BEFORE_PUNCT:
                ins_before = " "
                fixed += 1
            if after and after not in " \t" and after not in AFTER_PUNCT:
                ins_after = " "
                fixed += 1
            out.append(seg[pos:start])
            out.append(ins_before)
            out.append(seg[start:end])
            out.append(ins_after)
            pos = end
        out.append(seg[pos:])
        rebuilt.append(''.join(out))
    newlines.append(''.join(rebuilt))

open(path, 'w', encoding='utf-8').write('\n'.join(newlines))
print('spaces inserted:', fixed)

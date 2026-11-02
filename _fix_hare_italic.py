import re

path = 'h/hare.md'
text = open(path, encoding='utf-8').read()
lines = text.split('\n')
HAN = r'\u4e00-\u9fff\u3400-\u4dbf'
CJK = re.compile('[' + HAN + ']')


def mask(seg):
    s = re.sub(r'\*\*[^*\n]+\*\*', lambda m: '\x00' * len(m.group(0)), seg)
    s = re.sub(r'\$\$.+?\$\$|\$[^$]+\$', lambda m: '\x00' * len(m.group(0)), s)
    s = re.sub(r'\*[^*\n]+?\*', lambda m: '\x00' * len(m.group(0)) if ' ' in m.group(0) else m.group(0), s)
    return s


total = 0
newlines = []
for line in lines:
    segs = []
    if '`' in line:
        parts = line.split('`')
        for i, p in enumerate(parts):
            segs.append((p, i % 2 == 1))
    else:
        segs = [(line, False)]
    rebuilt = []
    for seg, iscode in segs:
        if iscode or not seg:
            rebuilt.append(seg)
            continue
        ms = mask(seg)
        # find spans to convert (iterate non-overlapping)
        out = []
        pos = 0
        for m in re.finditer(r'\*([^* \x00]+)\*', ms):
            t = m.group(1)
            if re.search(CJK, t):
                out.append(seg[pos:m.start()])
                out.append('**' + t + '**')
                pos = m.end()
                total += 1
        out.append(seg[pos:])
        rebuilt.append(''.join(out))
    newlines.append(''.join(rebuilt))

open(path, 'w', encoding='utf-8').write('\n'.join(newlines))
print('applied conversions:', total)

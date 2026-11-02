# -*- coding: utf-8 -*-
import json, io, os

BASE = r"D:\SEP-CN"

def read_text(p):
    with io.open(p, encoding='utf-8') as f:
        return f.read().split('\n')

def body_paragraphs(lines, skip_headings=True):
    """Return list of (lineno, text) for body paragraphs up to '## References' or first footnote def."""
    out = []
    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith('## References'):
            break
        if s.startswith('[^'):
            break
        if s == '':
            continue
        if s.startswith('#'):
            continue
        if s.startswith('*Mortensen'):
            continue
        # skip version bold line
        if s.startswith('**'):
            continue
        out.append(l)
    return out

src_lines = read_text(os.path.join(BASE, 'yuanwen', 'c', 'change.md'))
doc_lines = read_text(os.path.join(BASE, 'c', 'change.md'))

src_paras = body_paragraphs(src_lines)
doc_paras = body_paragraphs(doc_lines)

print("SRC body paras:", len(src_paras))
print("DOC body paras:", len(doc_paras))

# strip trailing newline chars
src_paras = [p.strip() for p in src_paras]
doc_paras = [p.strip() for p in doc_paras]

# step1 translations list (68)
step1 = json.loads(open(r"D:\SEP-CN\step1_change.json", encoding='utf-8').read())

assert len(src_paras) == 68, len(src_paras)
assert len(doc_paras) == 68, len(doc_paras)
assert len(step1) == 68, len(step1)

def yq(s):
    return json.dumps(s, ensure_ascii=False)

lines = []
lines.append("version: 1")
lines.append("slug: change")
lines.append("segments:")
for i in range(68):
    lines.append("  - id: %d" % (i+1))
    lines.append("    source: %s" % yq(src_paras[i]))
    lines.append("    step1: %s" % yq(step1[i]))
    lines.append("    step2: %s" % yq(doc_paras[i]))

out = "\n".join(lines) + "\n"
with io.open(os.path.join(BASE, 'tasks', 'c', 'change.ledger.yaml'), 'w', encoding='utf-8') as f:
    f.write(out)
print("WROTE ledger, segments:", 68)

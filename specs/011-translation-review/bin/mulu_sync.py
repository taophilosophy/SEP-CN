# -*- coding: utf-8 -*-
import io, re, sys
mt = io.open('mu-lu-s.md', encoding='utf-8').read()
sm = {}
for m in re.finditer(r'^\s*\* \[(.+?)\]\((\S+?)\)', io.open('SUMMARY.md', encoding='utf-8').read(), re.M):
    title, path = m.group(1), m.group(2)
    if title.startswith(chr(92)) or chr(8212)*2 + chr(35265) in title: continue
    sm.setdefault(path, title)
n = 0
for path in sys.argv[1:]:
    m = re.search(r'^(\s*)\* \[([^\]]*)\]\(%s\)' % re.escape(path), mt, re.M)
    if m and path in sm and m.group(2) != sm[path]:
        mt = mt[:m.start()] + '%s* [%s](%s)' % (m.group(1), sm[path], path) + mt[m.end():]
        n += 1
        print('fix', path)
io.open('mu-lu-s.md', 'w', encoding='utf-8', newline='').write(mt)
print('total', n)

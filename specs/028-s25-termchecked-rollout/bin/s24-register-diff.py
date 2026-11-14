# -*- coding: utf-8 -*-
"""s2.4 术语校辅助：斜体/粗体拉丁源术语 vs 两登记册（specs/028 S 面；ADR-0043）。

双层过滤（试点实测教训）：
  1. 记号过滤——类型论/逻辑记号（含括号/数字）非登记对象；
  2. 参考文献节豁免——照录书刊名不登记（ADR-0011）。
用法: python -I s24-register-diff.py <zh_doc>...（输出 JSON：每文件未登记源术语清单）
告警级：输出仅供 s2.4 人工裁定，不设门。
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))


def regs(path):
    terms = set()
    if not os.path.exists(path):
        return terms
    for line in io.open(path, encoding='utf-8'):
        m = re.match(r'^\|\s*([^|]+)\|', line)
        if m and not line.startswith('| --') and not line.startswith('| 原文'):
            v = m.group(1).strip()
            if v and v != '原文':
                terms.add(v)
    return terms


SHU = regs(os.path.join(ROOT, 'shu-yu-biao.md'))
REN = regs(os.path.join(ROOT, 'ren-ming-biao.md'))
KNOWN = {x.lower() for x in SHU | REN}
BIB = re.compile(r'^#{1,6}\s*(?:参考文献|Bibliography|References（引用注释）)\s*$',
                 re.M)


def scan(zh):
    txt = io.open(zh, encoding='utf-8').read()
    txt = re.sub(r'```[\s\S]*?```', '', txt)
    txt = re.sub(r'`[^`]*`', '', txt)
    body = BIB.split(txt)[0]  # 照录节豁免
    marked = set()
    for m in re.finditer(r'\*([^*\n]+)\*|\*\*([^*\n]+)\*\*', body):
        v = (m.group(1) or m.group(2)).strip()
        if re.search(r'[A-Za-z]{2}', v) and len(v) > 2 and not re.search(r'[()0-9]', v):
            marked.add(v)
    unreg = sorted(w for w in marked if w.lower() not in KNOWN)
    return {'zh_doc': zh, 'marked': len(marked), 'unregistered': unreg}


out = [scan(a) for a in sys.argv[1:]]
print(json.dumps(out, ensure_ascii=False, indent=1))

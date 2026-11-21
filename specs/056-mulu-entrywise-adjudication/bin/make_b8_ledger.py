#!/usr/bin/env python3
"""specs/056 b8 台账装配器：seq 1317–1504 全 KEEP（逐条证据已核，见 evidence-b8.md）。
节点映射按证据包现节；slug 取自 mu-lu-s.md 文档序，校验总数 188。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")

def slug_of(href):
    return href.rsplit("/", 1)[-1][:-3]

rows = []
for line in (ROOT / "mu-lu-s.md").read_text(encoding="utf-8").splitlines():
    m = ENTRY.match(line)
    if m:
        rows.append(slug_of(m.group(3)))
assert len(rows) == 1883, len(rows)

SECS = {}
def sec(lo, hi, name):
    for s in range(lo, hi + 1):
        SECS[s] = name
sec(1317, 1327, "正义理论")
sec(1328, 1332, "民主理论")
sec(1333, 1340, "自由主义与共和主义")
sec(1341, 1354, "政治义务与合法性")
sec(1355, 1364, "全球正义与移民")
sec(1365, 1370, "种族哲学")
sec(1371, 1377, "社会理论与公共哲学")
sec(1378, 1383, "经济哲学")
sec(1384, 1386, "文化哲学")
sec(1387, 1397, "法概念论")
sec(1398, 1402, "法学方法论")
sec(1403, 1406, "法与相邻学科")
sec(1407, 1411, "部门法哲学")
sec(1412, 1414, "惩罚与责任")
sec(1415, 1431, "美学")
sec(1432, 1453, "艺术哲学")
sec(1454, 1481, "女性主义理论")
sec(1482, 1491, "性别与酷儿哲学")
sec(1492, 1495, "性哲学")
sec(1496, 1504, "逻辑史与逻辑学家")
NOISE = {1441, 1443, 1491, *range(1454, 1482)}

lines = ["seq\tslug\t裁定\t新节\t依据\t凭证"]
for seq in range(1317, 1505):
    name = SECS[seq]
    nz = seq in NOISE
    basis = name + "随节" + ("，PP 区域冲突系噪音" if nz else "")
    cred = "本地摘要" + ("＋PP噪音注记" if nz else "")
    lines.append("%d\t%s\tKEEP\t\t%s\t%s" % (seq, rows[seq - 1], basis, cred))

out = ROOT / "specs/056-mulu-entrywise-adjudication/results/adjudication-b8.tsv"
out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print("b8 台账：%d 行，全 KEEP" % (len(lines) - 1))

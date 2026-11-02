# -*- coding: utf-8 -*-
"""从 yuanwen 英文源提取段落 source，与 _tr_concept*.py 译文合并，写段落账本。
分批增量：合并所有 _tr_concept*.py 的 T 字典；只写已翻译的 pid。"""
import json, glob, os, importlib.util

T = {}
here = r"D:\SEP-CN"
for f in sorted(glob.glob(os.path.join(here, "_tr_concept*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for k, v in m.T.items():
        T.setdefault(k, v)

src = open(os.path.join(here, "yuanwen", "c", "concept-emotion-india.md"), encoding="utf-8").read()
blocks = src.split("\n\n")

pid_block = {
 "p1":2,"p2":3,"p3":4,
 "p4":6,"p5":7,"p6":8,"p7":9,"p8":10,"p9":11,"p10":12,"p11":13,"p12":14,"p13":15,
 "p14":17,"p15":18,"p16":19,
 "p17":21,"p18":22,"p19":23,"p20":24,"p21":25,"p22":26,"p23":27,"p24":28,"p25":29,"p26":30,"p27":31,"p28":32,
 "p29":34,"p30":36,"p31":37,"p32":38,"p33":39,"p34":40,"p35":41,
 "p36":43,"p37":44,"p38":45,"p39":46,"p40":47,"p41":48,"p42":49,"p43":50,"p44":51,"p45":52,
 "p46":54,"p47":55,"p48":56,"p49":57,"p50":58,"p51":59,"p52":60,
 "p53":62,"p54":64,
}

entries = []
for pid in [f"p{i}" for i in range(1, 55)]:
    if pid not in T:
        continue
    blk = blocks[pid_block[pid]].strip()
    e = {"id": pid, "source": blk, "step1": T[pid].get("step1",""), "step2": T[pid].get("step2","")}
    entries.append(e)

lines = ["# 段落账本：concept-emotion-india（draft 阶段）",
         "# source 逐字取自 yuanwen/c/concept-emotion-india.md（英文源镜像，ADR-0009）",
         "# step1 = 忠实初译；step2 = 中文语言优化"]
for e in entries:
    lines.append("- id: %s" % e["id"])
    lines.append("  source: %s" % json.dumps(e["source"], ensure_ascii=False))
    lines.append("  step1: %s" % json.dumps(e["step1"], ensure_ascii=False))
    lines.append("  step2: %s" % json.dumps(e["step2"], ensure_ascii=False))

open(os.path.join(here, "tasks", "c", "concept-emotion-india.ledger.yaml"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("written entries:", len(entries))

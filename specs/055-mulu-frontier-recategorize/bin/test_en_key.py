#!/usr/bin/env python3
"""specs/055 en_key 回归测试：从 build_mapping.py 抽取 en_key 函数体单独验证，
不执行模块主体（一次性转换器，不可对新文件重跑）。"""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent / "build_mapping.py"
src = SRC.read_text(encoding="utf-8")
m = re.search(r"def en_key\(text\):.*?(?=\nfor e in entries|\n\S)", src, re.S)
assert m, "未找到 en_key 函数体"
ns = {"re": re}
exec(m.group(0), ns)
en_key = ns["en_key"]

CASES = [
    # (题名, 期望 en_key)
    ("科亨-施佩克尔定理（KS 定理） The Kochen-Specker Theorem (Carsten Held)",
     "the kochen-specker theorem"),
    ("可证性逻辑 Provability Logic (Rineke (L.C.) Verbrugge)",
     "provability logic"),
    ("女性主义视角下的物化 Feminist Perspectives on Objectification (Evangelia (Lina) Papadaki)",
     "feminist perspectives on objectification"),
    ("认识论 Epistemology (Matthias Steup、Ram Neta)", "epistemology"),
    ("模态认识论 The Epistemology of Modality (Antonella Mallozzi、Anand Vaidya、Michael Wallner)",
     "the epistemology of modality"),
    ("自由意志的不相容主义（非决定性）理论 Incompatibilist (Nondeterministic) Theories of Free Will (Randolph Clarke、Justin Capes、Philip Swenson)",
     "incompatibilist (nondeterministic) theories of free will"),
    ("沙夫茨伯里伯爵（第三代沙夫茨伯里伯爵安东尼·阿什利-柯柏） Lord Shaftesbury [Anthony Ashley Cooper, 3rd Earl of Shaftesbury] (Michael B. Gill)",
     "lord shaftesbury anthony ashley cooper, 3rd earl of shaftesbury"),
    ("乔瓦尼·弗朗切斯科·皮科·德拉·米兰多拉 Giovanni Francesco [Gianfrancesco] Pico della Mirandola (Francesco Molinarolo)",
     "giovanni francesco gianfrancesco pico della mirandola"),
    ("日志与编辑规划", "日志与编辑规划"),
]
fails = 0
for text, want in CASES:
    got = en_key(text)
    ok = got == want
    fails += 0 if ok else 1
    print(("OK " if ok else "FAIL"), repr(got), "" if ok else f"（期望 {want!r}）")
print("==", "全过" if fails == 0 else f"{fails} 失败")
raise SystemExit(1 if fails else 0)

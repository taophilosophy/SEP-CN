# P4 试金石记录（2026-11-17，归一后复测）

判定工具：`tools/check_pairs.py --gate`（体例轴硬档；ADR-0063/0065）。

| 试金石 | 形态 | 预期 | 实测 hard |
| ---- | ---- | ---- | ---- |
| `a/anscombe.md` | 点号编号＋canonical 尾序 | 0 | **0** |
| `a/abduction.md` | 曾裸号 `## 1 标题`（P7 已归一） | 0 | **0** |
| `a/abhidharma.md` | 曾脚注前置（P7 已移末位） | 0 | **0** |
| `s/social-procedures.md` | 作者括号含嵌套 `(L.C.)` | 0（检查器已容嵌套） | **0** |
| `t/tarski-truth.md` | 无尾节/无 pubinfo 异常件 | hard 0（软档 1：count-vs-source 容差） | **0** |
| `a/academic-freedom.md` | 桩件（仅 H1） | 豁免 | **0** |

合成件（译者注释节＋锚点）行为由单测覆盖：`tools/tests/test_adr0063.py`
`TestNoteSection` 8 例（对称/空节/缺节/断号/非句末/引块脚注忽略）＋节承载 2 例，
35 例全绿。

结论：六类判定全部与预期一致，无假阳性；试金石通过。

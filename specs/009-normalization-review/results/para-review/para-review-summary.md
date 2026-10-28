# 1% 人工深读汇总裁定（009）

主代理逐段通读 19 条随机样本（manual-1pct-sampling.json，种子 20261029），逐条裁定见 `manual-1pct.jsonl`。本文件为跨词条发现汇总与定性。

## 覆盖

| 词条 | 覆盖 | 备注 |
| ---- | ---- | ---- |
| malebranche、kant-aesthetics、disagreement-moral、parenthood、godfrey、lacan、existentialism-mexican、cordemoy、qt-idind、postmodernism、kukai、prioritarianism、james、umar-khayyam、bessarion、probability-medieval-renaissance、ethics-cultural-heritage、epistemology-social | md 全文逐段通读 | james 另做 R1 人工实证 |
| science-mechanisms | 正文全 448 行通读 | 510 行 defs 抽检 70 行（登记后续批次） |

## 真发现（移交修复责任会话，本战役零写入）

* **R1 重复 H1（30 词条，人工实证 james/anderson-john 型）**：词条包首块为图片时兜底标题叠加且图片先于标题。
* **R2 Related Entries 相对链接降级**（机理闭环）：html 绝对 URL 链接保留为 md 链接，相对 `../slug/` 链接降级为纯文本——19 条样本全数呈现该二态。
* **R3 键生成张冠李戴**：parenthood "hooks, bell, 1984" 得键 `holtug-1984`，机理移交管线会话查 build_cite_keys。
* **R4 键退化家族**：无作者条目首词键（lacan several-2025/bessarion platonis-nd 型 13+ 个）、名当姓（paul-1997=Verhaeghe、slavoj-1991=Žižek）、前缀截断（de-1904、la-1974、le-1996、lo-2015、bjo-2010）、非 ASCII 处理不一致（björnsson-2012 保 ö vs bjo-2010 剥 ö）、撇号截断（sant'-2019）。
* **R5 挂键率悬殊**（baseline 实证）：cite_markers 0（cordemoy/lacan）至 363（parenthood），link_citations 覆盖率全库不一致。
* **M2 裸美元**：lacan 3 处裸 `$`（matheme/fantasy 公式），行内公式失衡风险（007 的 232 math warn 同族）。
* **M3 零宽字符**：umar-khayyam L316 等混入 U+200B——建议 02-style 归一化检查增补零宽字符项。

## 定性修正与豁免登记

* **R6 图/表标签双现 → 上游结构保真**：html figlabel 与 figcaption 本为两段（figcaption 内容即 "Table 1."），转换逐字保真；完整形态见 science-mechanisms/epistemology-social（figlabel+实义题注+补充说明行）。中文翻译阶段合并渲染即可，非转换缺陷。
* **References/Notes 截尾规则获人工确认**：19 条全部按 T-07 设计转换（文献转脚注），defs 侧抽样核对形态统一。
* **上游形态保真清单**（中文翻译阶段甄别，非转换缺陷）：斜体 span 错位（`*.*`、`the* Science of Logic*`、`* Mind*` 带空格失效型）、括号错配（`(trans.]`、`</a>]`、双开括号）、双拼写并存（LoLorodo/LoLordo、Marc-Wogau/Wagau、Shpall/Spall）、笔误（the the、century century、apreatado、napantla、Benvensite、maniscript 等）、alt 占位文本（link to extended description below）、小节编号跳级（epistemology-social 3.3→3.5）、论证编号重起（umar-khayyam 跨 ol 重编）。

## 与机械层的关系（反机械层价值实证）

人工层捕获两类机械层系统性盲区，验证用户裁定：①R2 链接丢失（对齐器刻意忽略链接语法，永不可见）；②上游笔误/形态（骨架比对天然吸收）。机械层盲区对照层的设置成立。

## 后续批次

1. 跑批完成后（q–z 444 条在途）对 285 条 flagged 定点 `--force` 重跑（吸收对齐器三轮迭代）。
2. 分歧段逐条人工裁定落 adjudication.jsonl（分类承本文件定性，同模式批量裁定+代表例逐条复核）。
3. shape_report.py 生成 T-01…T-09 全库形态分布 → transpile-rules.md。
4. 无分歧段抽检 ≥3 段/条留痕（本文件 19 条记录已含抽检段阅读，逐段抽检凭证在 <slug>.json spot 字段）。

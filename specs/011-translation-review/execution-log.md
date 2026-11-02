# specs/011 执行记录

## 2026-11-02 开工：预清理与收口

* 门禁三红清零：术语硬错 3（Bernard Williams 人名表「威廉斯」vs 词汇表「威廉姆斯」冲突、登记册 conditional independence 重复行、人名表 Wolterstorff 重复行）+ 分类目录 1（james-ward 穆勒目录「瓦德」）全部修复；Williams 定案译名同步弱势方 39+5 处（integrity 正文 39 处、词汇表/SUMMARY/mu-lu-s/词条标题 4 处）。提交 71e104ff。
* 信息非对称识别：i/information-biological.md 的 Williams 1992 = George C. Williams（进化生物学）、i/implicature-optimality-games.md 的 Asher/Sher/Williams = 语用学作者，均非 Bernard Williams，不改；两人未在 ren-ming-biao 登记 → 人名反向校对层补登记。
* 工作区收口：26 条 s3_checked/done 逐条提交（a5/b1/d1/h3/i17）；48 条在途中间态快照 + check_style 改进 + i 批 monitor 提交 641faf13。
* 剩余未跟踪 345 文件为临时装配/分块脚本（_tr_*.py、_asm_*.json、trans_p*.json、tasks/e/_tr_*.json 等）——不提交；移交清单待收口时统一裁定清理。
* 战役 spec 建档。下一步：机械层全跑。

## 2026-11-03 机械层全跑与 style 修复（三版迭代）

* 扫描器 `bin/mechanical_scan.py`：152 条有实质译文词条（A41/B14/C26/D14/E8/F1/G1/H16/I23/J6/K1/S1）全量 check_style/check_math/check_academic。首跑：style 55 条 1602 处（italic-cjk 823、bold-spacing 406、curly-quotes 272、no-html 59、cjk-spacing 42）、math 8、academic 16（全为在途尾节缺失，预期态豁免）。
* **v1 事故与止损**：italic 修复器 ITALIC_RE 在 `**X**（*Y*）` 粗斜相邻结构跨对错配，且产生文本重复（al-khunaji「通达其在，我们也无需通达其」），复验门只查三类残余查不出此类损坏 → rules/05 基线还原：ledger 逆向回滚 56 段 + 41 个纯修复产物文件整体 checkout 还原至 83fc857^；final_star_audit/final_dup_audit 双终审（星号 tokenizer + ≥8 字重复，对照 83fc857^）确证 18+2 行破坏全部回收。
* **v3 安全形态**：italic 降级——行内已有粗体（粗斜共存）一律不自动替换，挂人工；星号结构不平衡（畸形）行整行跳过；仅纯斜体行自动替换。43 条 514 处，终审破坏/重复双零。人工清单 305 行（coexist/畸形/混合连坐）落 style-fix-manual.jsonl。
* check_style 工具改进三项：①bold-spacing 遮蔽数学区间星号误配（$w^{**}$）；②curly-quotes 转写撇号遮蔽（词内双侧拉丁/边界起始两规则，汉字邻接豁免——法语 l'âme、希伯来 Shi'ur、阿拉伯 Ya'qub 不再误报）；③影响全库门禁口径，复跑无回归。
* copernicus 直角引号「」32 对+『』1 对转弯引号；impossible-worlds 混合型 4 处、africana 12 处人工定点。
* math 8 条（alberic-paris/boolalg-math/change/computability/heytesbury/hilbert-program/impossible-worlds/information-semantic）移交管线会话（数学转换域）。

## 2026-11-03 术语同步与人名反向校对

* `bin/term_verify.py` 二重验证：term_coverage 全量缺口 834 术语 + 44 人名 → EN 正文级确认（yuanwen 剔 References）+ zh 正文级变体确认（登记册行全串、按顿号／分号拆分）→ 558 条缺口落盘 term-verify.jsonl（证据链完整）。
* **人名反向校对 26→25 条逐条裁定**：
  - A 类真缺口（译文用字 vs 登记册裁定偏差）修弱势方 5 处共 41 替换：腓茨拉尔夫→菲茨拉尔夫（crathorn）、狄迪穆斯→迪迪穆斯×4 + 泰奥弗拉斯托斯→特奥弗拉斯托斯×34（doxography-ancient）、卡姆斯勋爵→凯姆斯勋爵（aesthetics-18th-german）、德雷特斯基→德雷斯基（information-semantic）。
  - B 类非缺口（现代学者保留英文体例，体例明文允许）：Quine×2、Baier、Lewontin、Wright、Levinson、Habermas、Cavell、Koyré、Hull、Gilligan、Smith、Earman、Norton、Adams、Mersenne、Wiggins 等——**登记册汉译行与体例的张力移交 008 裁定**（登记行去留/用途标注）。
  - C 类漏译疑点（zh 正文无汉译无 EN 残留而 yuanwen 正文有）：Habermas@aesthetics-critical-theory、侯奈因@al-kindi、Theophrastus@democritus、Van Helmont@elisabeth-bohemia、ibn-ezra、Wiggins@identity——移交镜像完整性流程逐条回源核对。
  - 新发现人名异译重复行：Jean Hampton（L77 让·汉普顿 2026-11-01 vs L316 琼·汉普顿 justice-virtue 2026-11-02 凭证优先）——留 316 行裁定待执行。
* 双词术语 93 条（done/s3/r1 范围）：抽样定性三类——拉丁术语保留原文（prima facie 体例张力）、译名偏差（条件句分析 vs 条件分析@abilities）、英文残留——裁定尺度属 008 术语战役职权（需查证流程），011 以 term-verify.jsonl 证据链移交，不越权批量改译。
* 单词术语 ~440 条：EN 词边界匹配对普通词（play/completion）误报率过高，工具方法局限登记，移交。

## 门禁终态

* check_all 7 项：6 绿 + 学术规范 1 红（529 处全部为 48 条在途词条尾节缺失 + 已知在途态，f–k 六批接管会话（ses-FGHIJK-main-1103）推进中）。
* 本战役范围（152 条复核对象）内：术语硬错 0、词汇表滞后 17（告警级移交）、分类目录 0、星号/重复破坏 0。

# 两册去重（2026-11-13）

术语表与人名表内部重复清理。口径为用户 2026-11-13 裁定：人名表同人重复合并为一行、键形以**倒装键为主**并别名形；术语表**只并纯变体**（单复数、连字符、变音符拼写），带语域括注的多义分工行不动；冗余行删除并在保留行依据列留痕。

## 一、结果

| 册 | 合并组 | 删冗余行 | 行数变化 |
| ---- | ----: | ----: | ---- |
| 人名表 `ren-ming-biao.md` | 156 | 158 | 4690 → 4532 |
| 术语表 `shu-yu-biao.md` | 22 | 22 | 6215 → 6193 |

决策账（逐组保留键与旧键）：`specs/008-terminology-campaign/results/dedup-2026-11-13.json`；执行器：`bin/dedup_registries.py`（dry/apply，幂等：重跑 0 组）。

## 二、判重口径

* **人名表**：token 集合相等（`Adam Smith` = `Smith, Adam`）；或同主译名＋同姓 token＋名 token 有交集；或名 token 编辑相似度 > 0.8（`Koyré, Alexander` vs `Koyré, Alexandre`）。
* **术语表**：去标点折叠后相等（`anti-realism`/`antirealism`），或去尾 s 后相等且主译一致（`truth definition`/`truth definitions`）；键含语域括注者（`cardinal` vs `Cardinal（教会职衔）`、`dharma` vs `dharma（胜论性质）`）一律不参与。
* **已废弃行不参与**：保留旧译轨迹的「已废弃，见新行」行与活行不合并。首版脚本漏此规则，误并 Adorno 的旧译行与现行行，`check_terms` 废弃链硬错误实拦后回滚重做；门禁有效性得以验证。

## 三、留痕

保留行依据列追加「2026-11-13 重复行合并（旧键 …）」并更新裁定日期；键列以「 / 」并别名形（如 `Smith, Adam / Adam Smith`、`truth definition / truth definitions`），两种查法都可命中。合并后 `registry_azsort` 守恒重排（6193→6193、4532→4532，周界 0，重跑幂等），`check_terms` 硬错误 0，`check_all` 九项全绿。

## 四、遗留

* 术语表 4 组「译法不同」的疑似重复未并（`aesthetic judgments` 等带「单数同」注记者已并入；译法不一致组按冲突处理，不属去重）。
* 人名表合并后部分行籍属/生卒仍为「—」，属既存数据欠账（`specs/013` 清单）。

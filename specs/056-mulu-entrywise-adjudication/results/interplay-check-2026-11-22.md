# mu-lu-s 几方互转检查（2026-11-22）

检查器：`bin/check_mulus_interplay.py`（只读，可复跑）。几方＝`mu-lu-s.md`（正文）／`baseline/mulu-map.json`（归类账＋骨架）／`SUMMARY.md`（路径与文字源）／上游目录（G1–G2）。

## 结论：全部通过

| 组 | 项 | 结果 |
| ---- | ---- | ---- |
| I1 往返恒等 | 磁盘账重放 ＝ 文件（逐字节） | 通过 |
| I1 | 现抽账重放 ＝ 文件（逐字节） | 通过 |
| I1 | 磁盘账 ＝ 现抽账（rows＋skeleton 全等） | 通过 |
| I2 账内一致 | order 连续 0..1882、路径零重复、骨架锚合法且单调 | 通过 |
| I2 | indent 仅 0／2（1712 独立＋171 簇成员） | 通过 |
| I3 文字跟随 | 账内文字 ≡ SUMMARY 文字（转义归一） | 0 不一致 |
| I3 | 账内路径均可在 SUMMARY 找到 | 0 缺失 |
| I4 负向探针 | text／indent／swap／skeleton／delete 五种微扰 | 全部被重放捕获（判据非空转） |
| 结构不变量 | 缩进成员无孤儿（向上必达 ind=0 母条）、无深度>2 | 0 违规 |
| 标准门禁 | G1–G4、check_mulu_s 六项、check_all 17 项 | 全绿 |

## 观察（非缺陷）

- 簇结构：59 簇／171 成员；最大簇康德 22、亚里士多德 16、柏拉图 14。
- 跨字母目录簇成员 28 条（如 `protagoras`→`sophists`、`democritus`→`atomism-ancient`、`sufficient-reason`→`leibniz`）：属"概念随主题/人物母条"的正常形态，与字母目录无绑定关系。
- check_mulu_s [3] 的 4 条"SUMMARY 有而 mu-lu-s 无"为既知非词条件（mu-lu-s 自身、版权说明、项目日志两卷），不计硬错。

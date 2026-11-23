# specs/058 提取总表口径与计数（2026-11-22）

- 语料：yuanwen/ 全库，2418 篇
- 去重键：register_lib.norm_key_quote（A 口径，引号与变音符折叠）
- 保留候选：260526 条；因低频短语下限未列出：2774918 条（freq<5 且无术语后缀的二元/三元片段）
- 类型分布：phrase 97763，term 69824，sentence 45970，person 22088，foreign 15239，work 4701，topic 3113，cjk 1256，arabic 468，greek 99，cyrillic 2，hebrew 2，devanagari 1
- 档位分布：T1 17036／T2 88960／T3 57591／T4 96939
- 状态分布：已登记 7212／池内 55589／本轮新增 197725

## 状态说明

- 已登记（术语表／人名表）：折叠键命中登记册既有行。
- 池:published/held/rejected/new：命中 tasks/term-pool.json 的既有状态。
- 本轮新增：两处均未命中，属第二轮新提取候选，需按 A/B/C 分档裁定。

## 未列出部分

低频短语片段（freq<5 且尾词无术语后缀）留在 candidates.json.gz 之外的统计中，不进入总表；这是刻意的精度取舍，不是丢弃证据：candidates.json.gz 记录了 kept 全量，未列出部分仅计数。

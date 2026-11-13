# 备查：2026-11-14 替代源核实中的「查无」条目

任务：`specs/013-person-attribution/results/verify-2026-11-14-alt.tsv`
规则：依据 ADR-0031 档位；维基百科不作依据；逐人核实，取不到即记「查无」，不推测。

## 未写入 TSV 者（1 人）

### Barrio, Eduardo

- **查无项**：籍属、生卒/鼎盛年（两项均无可采信凭证）。
- **已查来源与结果**：
  1. **GND**（德国国家图书馆规范档，经 lobid.org 接口）：
     - `q=Barrio, Eduardo`：7 条命中，均为同形异人（Matos Barrio, Eduardo，1904–1995，西班牙摄影师；Barrios, Eduardo，1884–1963，智利作家；Barriobero y Herrán, Eduardo，1875–1939，西班牙法学家；Barrionuevo, Eduardo E.，阿根廷政治人物等），无逻辑学家。
     - `q=Barrio, Eduardo Alejandro`：0 条。
     - `q=Eduardo Barrio`：7 条，仍无目标人物。
  2. **BnF 规范档**（法国国家图书馆，SRU `aut.personalName all "Barrio, Eduardo"`）：0 条。
  3. **BnF 书目**（`aut.personalName all "Barrio" and bib.title all "logics"`）：0 条。
  4. **LC NAF**：`https://id.loc.gov/search/?q=Barrio%2C%20Eduardo&q=cs:http://id.loc.gov/authorities/names&format=json` 返回 429，随后为 Cloudflare 人机验证页，未能读取（未反复重试）。
  5. **本地来源页**：`en/logic-substructural/index.html:1448`、`:1453` 仅见参考文献 `Barrio, Eduardo; ...`，无籍属或生卒叙述。
- **结论**：线索称「逻辑学家，阿根廷」，但无档位内权威源可回溯，故不写入 TSV；待 LC NAF 可达或取得大学出版社作者页后再补核。
- **日期**：2026-11-14。

## 附：部分字段查无（已入 TSV，籍属可核、生卒未载）

| 键 | 可核字段 | 查无字段 | 说明 |
| --- | --- | --- | --- |
| Barber, Alex | 籍属：英国（GND gnd 1290984093，地理区码 Großbritannien） | 生卒/鼎盛年 | GND 无生卒；SEP 本地页仅示作者身份与 Open University 链接。 |
| Bartel, Christopher | 籍属：美国（GND gnd 1224834682，地理区码 USA） | 生卒/鼎盛年 | GND 无生卒；SEP 本地页仅见引用（Bartel 2011）。 |

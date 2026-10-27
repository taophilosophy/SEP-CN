# 0010. yuanwen 图片相对引用采用 ../assets/

状态：accepted | 日期：2026-10-28

## 背景

ADR-0009 第 4 条规定词条图片"md 内 `assets/<slug>/<文件名>` 相对引用"——该写法制定于根级 `<slug>.md` 时代，图片目录与词条文件同级，`assets/` 前缀恰好成立。ADR-0009 把词条移入 `<letter>/` 字母子目录后，`yuanwen/<letter>/<slug>.md` 到 `yuanwen/assets/<slug>/` 的正确相对路径跨了一级目录，`assets/` 写法在几何上失效（会解析到 `yuanwen/<letter>/assets/`，不存在）。

2026-10-28 yuanwen 全量复核（技术债务 D15）实测：已接线文件中 `assets/` 与 `../assets/` 两种写法并存，前者全部为死链；转换器 `tools/yuanwen.py` 同期修复了正文 `<img>` 接线缺失（10019 图未接线），统一输出路径形式时必须裁定采用哪一种。

## 决策

1. **`yuanwen/<letter>/<slug>.md`（及 `<slug>.<x>.md`）内的图片相对引用一律为 `../assets/<slug>/<文件名>`**（补充材料与主文件同目录，同用该形式）。
2. 站点框架图标（`../../symbols/…` 等）不属镜像职责，不本地化、不引用。
3. 本 ADR 修订 ADR-0009 第 4 条的引用前缀写法；本地化位置（`yuanwen/assets/<slug>/`、上游同名）不变。

## 后果

* `tools/yuanwen.py` 行内 `<img>` 接线与 `figure` 图输出统一为 `../assets/<slug>/`；2026-10-28 起全量重转换后的产物即合规形态。
* `rules/01-repository-structure.md` 的图片条款同步改写并标注本 ADR。
* ADR-0009 第 4 条的 `assets/<slug>/` 写法自本 ADR 起废止，其余条款不受影响。

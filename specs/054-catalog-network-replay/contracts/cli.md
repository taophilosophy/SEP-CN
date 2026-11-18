# specs/054 — CLI 契约

## parser.py（升级，向后兼容）

```text
parse_catalog(html_text) -> [{slug,title,authors,alias_of,level}]   # 签名与输出序不变（slug 序）
```

升级点（只增不改，消费方零破坏）：

- 每 item 增 `doc_order`（页序位，0 起，按 `<li>` 关闭顺序）、`has_children`（该 li 是否带嵌套 `<ul>`，带链接簇母为 true）；
- 别名行族：除并入正典条目 `aliases[]`（现状保留）外，顶层增 `alias_rows[]`＝{slug, label, href_text, level, doc_order}（653 行全量，重复 slug 各占一行）；
- 纯文本母行（此前被 `_finish` 丢弃）：顶层增 `cluster_mothers[]`＝{label, level, doc_order}（188 条）。

## fetch_catalog.py（沿用）

```text
python tools/fetch_catalog.py --reparse    # 离线：用 en/_catalog 最新快照重新解析写 baseline/catalog.json
python tools/fetch_catalog.py              # 联网抓取（另轮）
```

`--reparse` 不联网、不改快照；输出账含 §parser 升级三族字段。验收用 `--reparse-snap <文件名>` 指定快照（新增，默认仍取最新），供 A3 跨时点装配从旧快照重建同时点账。

## rebuild_catalog.py（新增，目录域装配器）

```text
python tools/rebuild_catalog.py --build                     # 从最新快照生成 baseline/catalog-skeleton.json
                                                            #   ＋ baseline/catalog-residual.json（并冻结）
python tools/rebuild_catalog.py                             # 重放：账⊕规则⊕池 → stdout 汇总 JSON
python tools/rebuild_catalog.py --check [--snap <文件名>] [--offline-account <账文件>]
                                                            # sha256 与钉存快照逐字节对比；全等退出 0
```

- 装配件只输出 sha 与汇总，**禁止写回** `en/_catalog/`（oracle 只读，specs/053 返工理论）；
- 池准入谓词（053 A5）：kind ∈ {`no-close-li`, `inline-markup`}，正文文字层禁入；`--build` 后池冻结，改动须登记；
- 规则层：实体编码策略（HTML4 命名优先＋十进制兜底）、level 缩进（2→3 空格）、ul 开闭与收口形态、letter 节标与固定说明行（skeleton 账锚点插入）。

## check_catalog_network.py（新增，四向重放门）

```text
python tools/check_catalog_network.py --gate    # 四子门全绿退出 0；判官只读
```

- **G1 装配等值**：rebuild_catalog --check（最新快照＋旧快照各一）；
- **G2 en-SUMMARY 重放**：`gen_en_summary.py --check` 退出码直通；
- **G3 mu-lu 重放**：baseline/mulu-map.json ⊕ SUMMARY.md → 重建 mu-lu-s.md 目录行，与现文件逐行全等（前言等非目录段按模板账冻结比对）；
- **G4 目录↔SUMMARY 对账**：catalog.json 条目集 ↔ SUMMARY slug 行集双向差＝0（映射判定沿用 summary_sync report 规则：反向唯一命中才算成立，同题歧义转人工不计入）。

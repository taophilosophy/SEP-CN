# T206 全量验证

- 日期：2026-11-27。
- 门禁：`python tools/check_all.py` **23/23 全绿**（含 layout、summary、mulu、academic、divergence、fidelity、en-integrity、en-patches、pairs、ledger、catalog-net、term-concepts、unit tests）。
- 单测：`python -m unittest discover -s tools/tests` 全绿（729 tests）。
- 站点：壳仓 `SEP_SHARD=ad bun run docs:build` 成功，`build complete in 271.03s`；无死链；产物含 `dist-ad/zh/a/abduction.html`、`dist-ad/en/a/abduction.html`、`dist-ad/zh/mu-lu-s.html`、`dist-ad/zh/shu-yu-biao.html`、`dist-ad/zh/SUMMARY.html`、`dist-ad/zh/PROGRESS.html`。
- URL：中文 `/zh/…`、英文 `/en/…`；根首页 `/` 仍由 `README.md` 生成（CI `cp docs/README.md docs/index.md`）。
- GitBook：根 `.gitbook.yaml` 的 `summary: zh/SUMMARY.md` 可解析；`en/.gitbook.yaml` 的 `SUMMARY-en.md` 可解析（`gen_en_summary --check` 最新）。
- 抽样：`zh/<letter>/<slug>.md`、`en/<letter>/<slug>.md`、`html/<slug>/index.html` 三路径均可解析；`baseline/entries.json` 1873 件 `zh_doc`／`yuanwen.md` 全部改写。
- 已知边界：本机只跑 ad 分片，四片合并与 Pages 部署以 CI 为最终裁判；旧 `/a/…`、`/yuanwen/a/…` URL 按用户裁定不再保留。

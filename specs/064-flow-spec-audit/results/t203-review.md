# T203 双写互换与站点常量

- 日期：2026-11-27；起始 commit：`df3dce234b2fed79903eb304939ab7cda4674ab8`。
- 目录：`git mv en __swap_en_yuanwen__` → `git mv yuanwen en` → `git mv __swap_en_yuanwen__ yuanwen`；旧 `en` HTML 现为 `yuanwen/`，旧 `yuanwen` Markdown 现为 `en/`（含 `SUMMARY.md`、`SUMMARY-en.md`、`.gitbook.yaml`、`assets/`）。
- `SUMMARY.md` 复制为 `zh/SUMMARY.md`，根链接改 `../`；后续 T204 归集。
- `.vitepress`：`config.mts` 分片、SUMMARY 解析与归一、配对、侧栏、`srcExclude`、`locales`、`watch`、导航与 `catLink` 全部改新路径；`prepare-gitstamps.mjs` 排除 `yuanwen/`；`VersionPin.vue` 镜像判定改 `en/`。
- 工具：`fetch_entry` 写 `yuanwen/`、`yuanwen.py` 读 `yuanwen/` 写 `en/`、`common.find_zh_doc` 读 `zh/SUMMARY.md`；相关 `check_*` 逐步修正（详见 T204/T206）。
- 验收：`check_all` 23/23；VitePress ad 分片构建成功（2026-11-27，`build complete in 271.03s`）。

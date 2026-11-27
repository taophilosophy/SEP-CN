# 临时布局迁移方案（S16，2026-11-27 用户裁定）

- 目标：`en/` 与 `yuanwen/` 互换目录名；根目录词条目录归入新建 `zh/`；同步更新工具链、日志、记忆、文档、任务书、specs、`.vitepress` 与壳仓 `taophilosophy.github.io`。
- 用户裁定：① 先双写验证（不直接删旧）；② 迁入范围含 `a–z`、`1`、`fang-fa-lun`、`guan-yu`、`jian-yi-shu`、`qian-yan`；③ 历史文本一并改写；④ `SUMMARY.md` 随词条目录迁入 `zh/`；⑤ 站点接受新 URL 前缀 `/zh/…`、`/en/…`（不保留旧 URL，旧外链失效为已知代价）；⑥ `.vitepress` 与壳仓一并修改。
- 性质：**临时阶段**，S16；T202–T207；开始／结束各打 `batch/064-migrate-start|end`。

## 1 目标布局

| 旧路径 | 新路径 | 说明 |
| ---- | ---- | ---- |
| `en/<slug>/…`（HTML 源） | `yuanwen/<slug>/…` | 目录名互换：`yuanwen` 承接 HTML |
| `yuanwen/<letter>/<slug>.md`（镜像） | `en/<letter>/<slug>.md` | 目录名互换：`en` 承接 Markdown 镜像 |
| `yuanwen/SUMMARY.md`、`SUMMARY-en.md`、`.gitbook.yaml`、`assets/` | `en/` 同名 | 英文空间配置与导航随目录互换进入 `en/` |
| `<letter>/<slug>.md`、`1/**` | `zh/<letter>/<slug>.md`、`zh/1/**` | 词条正文归入 `zh/` |
| `fang-fa-lun/`、`guan-yu/`、`jian-yi-shu/`、`qian-yan/` | `zh/<同名>/` | 中文目录一并归集 |
| `SUMMARY.md` | `zh/SUMMARY.md` | 中文导航随正文归集；条目链接改为相对 `zh/` |
| `README.md`、`mu-lu-s.md`、`shu-yu-biao.md`、`ren-ming-biao.md`、`PROGRESS.md`、`RELEASE-NOTES.md`、`AGENTS.md` | 不变 | 根级说明页与登记册留在根目录 |
| `assets/`、`baseline/`、`journal/`、`rules/`、`specs/`、`tasks/`、`tools/`、`.vitepress/` | 不变 | 非词条正文 |
| `.gitbook.yaml` | 不变（`summary: zh/SUMMARY.md`） | 中文 GitBook 空间；英文空间改由 `en/.gitbook.yaml` 承担 |
| 壳仓 `docs/`（子模块／本地目录联接） | 不变 | 壳仓命令与工作流路径不随布局改写 |

**站点 URL**：中文页 `/zh/<letter>/<slug>`，英文页 `/en/<letter>/<slug>`；根级页 `/README`、`/mu-lu-s` 等不变。旧 `/a/abduction`、`/yuanwen/a/abduction` 失效，由用户在 T207 后另行决定是否加跳转。

## 2 双写与回退

1. **T202 备份**：`en/`、`yuanwen/`、27 个字母目录、4 个中文目录、`SUMMARY.md`、`.gitbook.yaml`、`.vitepress/` 清单化并复制到 `state/layout-backup/2026-11-27/`；同时记录壳仓 HEAD 与 `deploy.yml`／`README.md` 的路径引用现状；生成 SHA-256 清单与回退脚本。
2. **T203 双写**：以旧 `yuanwen/` 生成新 `en/`，以旧 `en/` 生成新 `yuanwen/`；复制 `SUMMARY.md` 为 `zh/SUMMARY.md`；旧目录保留，可随时回退。
3. **T204 归集**：移动 27 个字母目录＋4 个中文目录到 `zh/`；改写 `zh/SUMMARY.md` 与根级说明页链接；同步 `rules/layout.json`、扫描器与任务 JSON。
4. **T206 验证**：全量门禁、单测、`zh`／`en`／`yuanwen` 三路径抽样、VitePress 分片构建与壳仓构建；不过即从备份回退。
5. **T207 收口**：二次确认后删除备份与旧目录；提交并推送本仓与壳仓；打 `batch/064-migrate-end`。

## 3 工具链与关联者

### 3.1 `.vitepress`（本仓，站点配置层）

| 文件 | 必改点 |
| ---- | ---- |
| `config.mts` | 分片 `shardExclude`：`${l}/**`→`zh/${l}/**`、`yuanwen/${l}/**`→`en/${l}/**`；非字母目录与根级页面同步；`parseSummary` 改读 `zh/SUMMARY.md`、`en/SUMMARY.md` 并把 href 归一为仓库根相对路径；配对正则改 `^en/.+\.md$`；字母桶 `seg` 改取 `zh/` 后第一段；`zhSidebarByLetter`／`dirSidebars` 键改 `/zh/…/`；英文侧栏与 `i18nRouting` 键改 `/en/`；`siteExclude` 改 `yuanwen/**` 并排除 `zh/SUMMARY.md`、`en/SUMMARY.md`、`en/SUMMARY-en.md`；`locales` 键 `yuanwen`→`en`；`watch.ignored` 改 `**/yuanwen/**` |
| `theme/components/VersionPin.vue` | 镜像判定 `relativePath.startsWith('yuanwen/')`→`startsWith('en/')` |
| `prepare-gitstamps.mjs` | 排除目录 `'en/'`→`'yuanwen/'`；`en/`、`zh/` 作为站点页面保留 |
| `.vitepress/README.md` | 分片、srcExclude、双语配对、反向入口等全部路径示例改新布局 |
| `config.build-check.mts`、`merge-shards.mjs`、`math-plugin.mjs` | 无硬编码布局路径，T206 复核即可 |
| `theme/components/BilingualCompare.vue`、`bili-paragraph.ts` | 只消费 frontmatter `enPath`／`zhPath`；`zhPath` 注入值改 `/zh/…`，组件逻辑不变 |

`baseline/entries.json` 的 `zh_doc` 与 `yuanwen.md` 字段名保留，值分别改 `zh/…`、`en/…`；`config.mts` 的 `srcByDoc` 逻辑不改。

### 3.2 `tools/` 与结构事实源

- `tools/`：`repo_path("en"|"yuanwen")` 语义反转；字母目录扫描改 `zh/`；`axis_lib`、`fetch_entry`、`yuanwen.py`、`check_*`、`clean.py`、`progress.py`、`summary_sync.py`、`rebuild_dir.py`、`gen_en_summary.py` 全部核对。
- `SUMMARY.md`：改为 `zh/SUMMARY.md`；词条链接去 `zh/` 前缀（相对自身），根级页面链接补 `../`。
- `rules/layout.json`：`letter_dirs.path` 改 `zh/<letter>`；新增 `zh` 根条目并登记 `en`／`yuanwen` 新语义；`check_summary`／`check_layout`／`check_junk` 同步。
- `tasks/**/*.json`：`zh_doc` 全部改 `zh/<letter>/<slug>.md`；账本 `source` 文本不变。
- `journal/`、`specs/`、`rules/`、`README.md`、`AGENTS.md`、`.vitepress/README.md`、项目记忆：旧路径与 `en`／`yuanwen` 语义一并改写；生成“旧→新”映射表，保留可审计性；不重写 Git 历史。

### 3.3 壳仓 `taophilosophy.github.io`

| 文件 | 处理 |
| ---- | ---- |
| `.github/workflows/deploy.yml` | 不改路径：`cp docs/README.md docs/index.md` 仍成立，分片名 `ad/ek/lp/qz` 与环境变量不变；T206 复核确认 |
| `README.md` | 更新布局说明：`zh/` 中文正文、`en/` 英文镜像、`yuanwen/` HTML 源；说明站点 URL 新前缀；构建命令不变 |
| `package.json`、`.gitmodules`、本地 `docs` 目录联接 | 不变 |
| 提交 | 壳仓单独提交并推送（只含 README 等壳侧改动；`docs` 指针随本仓推送后由 CI 定时拉取） |
| 构建验证 | `bun run build` 全量或四片 `SEP_SHARD=… bun run docs:build`＋`merge-shards`；记录耗时与结果 |

### 3.4 文档与记忆

- `README.md` 与根级登记册中的词条链接改 `/zh/…` 或相对 `zh/…`；`mu-lu-s.md`、`PROGRESS.md` 同步。
- `rules/01-repository-structure.md`、`rules/README.md` 规则地图、`AGENTS.md` 结构形态与硬约束表同步新路径语义。
- `journal/` 与 `specs/` 历史文本一并改写；旧路径只保留在“旧→新映射表”和 ADR 变更说明中。
- 项目记忆（`.workbuddy` 等）中如存旧路径，T205 一并更新。

## 4 验收

- `check_all.py` 23/23；`unittest discover` 全绿；`check_summary`／`check_layout`／`check_images` 0。
- 所有 `tasks/**/*.json` 的 `zh_doc` 可解析；`zh/SUMMARY.md` 无失效链接。
- VitePress 分片构建（至少 `ad`，最好四片）通过；`/zh/…` 与 `/en/…` 页面存在；死链检查 0；`git-stamps` 覆盖 `zh/`、`en/`。
- 壳仓 `bun run build` 通过；`deploy.yml` 无需改路径；壳仓 README 与新布局一致。
- GitBook：根 `.gitbook.yaml` 的 `zh/SUMMARY.md` 可解析；`en/.gitbook.yaml` 的 `SUMMARY-en.md` 可解析。
- 抽样 11 件：`zh/<letter>/<slug>.md`、`en/<letter>/<slug>.md`、`yuanwen/<slug>/index.html` 三路径均可解析。
- 历史文本中不再出现旧路径（映射表与归档说明除外）。

## 5 风险与边界

- **URL 前缀变更**：旧 `/a/…`、`/yuanwen/a/…` 外链失效；用户已接受，跳转另批处理。
- **根级相对链接**：中文词条移入 `zh/` 后，指向 `../README.md` 等根级文件的链接需改 `../../`；VitePress 死链检查会硬拦。
- **GitBook 中文空间**：`root: ./` 不变，`summary: zh/SUMMARY.md` 已就位；`zh/SUMMARY.md` 内根级链接用 `../`。
- **英文空间**：`yuanwen/.gitbook.yaml` 随目录互换进入 `en/`，HTML 侧不得残留同名配置；T202/T206 各查一次。
- **硬编码路径最多**：先跑只读门禁再改任务 JSON；任何一步失败从 `state/layout-backup` 回退。
- **壳仓独立版本库**：`docs/` 本地为目录联接，壳仓提交只含壳侧文件；CI 用真实子模块，需本仓推送后再验证站点。
- **VitePress 路由与相对路径**：本次不做 `rewrites`，接受 `/zh/`、`/en/` 前缀；`transformPageData` 注入的 `enPath`／`zhPath` 必须用新前缀。

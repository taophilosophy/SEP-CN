# 064 组 B 执行证据（2026-11-27）

- 组：**b**（S2 清理检查点；T020–T024；W0b 并行卫生轨）
- start tag：`batch/064-b-start` → `3aec11279`（已推送）
- end tag：待打（本文件提交后打 `batch/064-b-end`）
- 门禁：`python tools/check_all.py` **23/23 全绿**（新增 clean 门禁后）
- 授权：B 组由主代理单干；本轮未调用子代理（ADR-0034）

## 1 T020 clean.py 契约

**状态：完成**。`tools/clean.py` 改为：

| 模式 | 行为 | 退出码 |
| ---- | ---- | ---- |
| 默认／`--check` | 只读列出目标；有垃圾也报告 | 0 |
| `--check --strict` | 只读；仅保护件缺失／目标越界时红 | 0／1 |
| `--go` | 删除未跟踪垃圾（目录整体删除，不触碰跟踪文件） | 0；删除失败 1 |
| `--go`＋`--check/--strict` | 用法错误 | 2 |

- 保护件：`en/`、`yuanwen/`、`baseline/`、`SUMMARY.md`；`baseline/` 同时加入遍历跳过集。
- 不消费登记表（G23 未建表）。
- 修复旧实现“垃圾目录被剪枝但非空目录删不掉”的缺陷：垃圾目录整体作为目标，`--go` 用 `shutil.rmtree` 删除；若目录含跟踪文件则跳过。
- 单测：`python -m unittest tools.tests.test_clean -v` → **8/8 OK**（覆盖 `*.tmp` 默认 0、strict 保护件缺失退 1、`--go --check` 用法错误 2）。

## 2 T021 扫描面

**状态：完成**。垃圾目录集合：

`target/`、`__pycache__/`、`.pytest_cache/`、`.mypy_cache/`、`.ruff_cache/`、`.vitepress/cache/`、`.vitepress/dist/`、`.screenshots/`（本地截图工具临时目录）。

实测：在根目录创建上述目录及占位文件后运行 `python tools/clean.py --check`，目标数由 91 增至 97，逐项列出 `.mypy_cache`、`.pytest_cache`、`.ruff_cache`、`.vitepress/cache`、`.vitepress/dist`、`__pycache__` 等；退出码 0；`--check --strict` 退出码 0。测试后已删除占位目录。

## 3 T022 GATES 评估与接入

**状态：完成（接入）**。

| 项 | 结论 |
| ---- | ---- |
| 预期命中 | 硬失败 0；本地常态垃圾 91 项仅报告，不改变退出码 |
| 本地／CI 同档 | strict 只看保护件 `en/`、`yuanwen/`、`baseline/`、`SUMMARY.md`，本地与 CI 检出均有；垃圾数量差异不影响退出码 |
| 接入 | `tools/check_all.py` GATES 增 `("缓存与临时物", "clean", "tools/clean.py --check --strict")`，位于 junk 之后 |
| 编号 | 以 `--list-gates` 实际输出为准：新增 key `clean`；`check_all` 现 **23 项**（22 GATES＋管线单元测试） |
| 幂等 | 只读；`--strict` 不删除任何文件 |

## 4 T023 .gitignore

**状态：完成**。新增：

- `target/`（Rust 构建产物，任意层级）
- `/.screenshots/`（本地截图/浏览器工具临时目录）

`git check-ignore -v` 实测命中：`target/foo`、`.screenshots/x`、`__pycache__/x.pyc`、`.vitepress/cache/x`、`.vitepress/dist/x`、`.ruff_cache/x`、`.mypy_cache/x`、`.pytest_cache/x`；`git status` 不再出现这些路径。

## 5 T024 checks.yml

**状态：完成（不新增步骤）**。`checks.yml` 的矩阵由 `check_all.py --list-gates` 展开（ADR-0061），clean 门禁自动成为独立矩阵作业；不手写重复步骤。`rules/05/ci-workflows.md` 已登记 clean 门禁；`rules/05/tools.md` 与 `tools/README.md` 已同步 clean 契约。

## 6 状态与残留

| 项 | 结果 |
| ---- | ---- |
| T020–T024 | 全部完成 |
| B 组闸门 | 无独立闸；B 组出口＝五项完成＋23/23 门禁 |
| `batch/064-b-end` | 待打（本文件提交后） |
| 未执行 | 未在仓库上跑 `clean.py --go`；91 项本地垃圾仍保留，待用户另行授权清理 |
| 未改 | `en/`、`yuanwen/`、译文、`tasks/*.json`、`baseline/` |

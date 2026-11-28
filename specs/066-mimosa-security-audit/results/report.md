# Mimosa 全库深度安全审计报告（2026-11-28）

本报告是 `specs/066-mimosa-security-audit/spec.md` 的分析面：记录扫描凭证、2353 条 finding 的逐类归因、真实缺陷修复与残余风险。逐条处置见同目录 `findings-triage.csv`。

## 1 结论摘要

1. **未发现可远程利用的已证实漏洞。** 2353 条 finding 全部是静态候选，`validation.investigated=0`；本报告不作“全项目安全”结论。
2. **真实缺陷 5 类，已修复 5 类：**
   * 3 个脚本关闭 TLS 证书/主机名校验，其中 `tl_jwt_crawl.py` 会随请求发送 JWT；
   * `tools/fetch.py` 对动态 URL 无协议/主机边界，且重定向不受控；
   * `tools/fetch_entry.py` / `fetch_audit.py` 把上游 HTML 的相对资产路径直接拼入落盘路径，可被 `../` 带出词条包；
   * `format.yml` 把 PR 文件名插值进 `run` 脚本，存在表达式注入；`create-pdf.yml` 把 dispatch 输入插值进 Python；
   * 8 个工作流的 25 处第三方 Action 使用可移动标签，未钉到 commit SHA。
3. **1 起凭证/隐私事件需用户处置：** 已提交证据文件含一枚服务端已判无效的 JWT 与形似手机号的 username；本 PR 不重写历史、不再次展示该值，须轮换会话并评估历史清理（§5.2）。
4. **2183 条属范围外或扫描器误报；165 条按威胁模型接受；5 条已修复：** 本地未跟踪件 2096、第三方 MathJax 20、符号碰撞 24、入口摘要 26、固定路径 9、固定主机 6、废弃代码 1、非安全随机 1；操作者路径 165 条按本机 CLI 威胁模型接受；fetch 白名单、协议过滤、包含性校验共 5 条进入修复。
5. **项目门禁全绿：** `check_all.py` 24 项；新增安全回归 7 条；受影响模块 64 条测试通过。

## 2 扫描凭证与覆盖

| 项 | 值 |
| ---- | ---- |
| jobId | `scan-job-mx09ygem-0497c47618001614` |
| scanId | `scan-2026-11-28T10-39-14.673Z-fa8d19675d8e` |
| 快照 commit | `07d65c0475fc9286861a26fabb3f729dfe331211` |
| 封印 | `sha256:14bf59315b734be9041b6327f231b22b53df7b4465f8dc82cdfee836b69323b7` |
| 深度/状态 | `deep` / `inconclusive`（coverage `partial`） |
| 文件覆盖 | selected 4169 / parsed 4169 / read 0 失败 / parse 0 失败 / 未截断 |
| 依赖 | 143 包；offline advisory matched 0 |
| finding | 2353（high 1550、medium 798、low 5） |

**HTML 排除证据：**

1. Mimosa 原生支持扩展名不含 `.html`；`coverage` 的 `selectedFiles` 与物理代码文件口径吻合，9547 个 `.html` 不在其中。
2. 2353 条 finding 的 `location.path` 后缀统计：`.py` 1391、`.js` 962，`.html` **0**。
3. 试金石：临时目录放 `app.js`（含 SQL 注入）+ `danger.html`（含 `eval`），深扫 `selectedFiles=1`，只解析 `app.js`。

**覆盖缺口：**

* `.vitepress/` 点目录未入根扫描，已用 Semgrep 补扫 21 个源文件。
* `.ps1` 无 Semgrep 语法支持，6 个 spec-kit 脚本 + 1 个 014 脚本逐文件人工审读。
* `.md/.json/.ndjson/.yml/.tsv` 不是代码规则对象；以 PII、供应链、交付链、git 历史与项目门禁另行覆盖。
* `mimosa git-secrets` 本机失败（0 commits），见 §5.3。

## 3 2353 条 finding 的处置

| disposition | 条数 | 依据 |
| ---- | ----: | ---- |
| `OUT_OF_SCOPE_LOCAL` | 2096 | `script/` 1104、`script/tmp/probe` Chrome 用户目录 940、`state/` 52；均 gitignore，不随仓库分发 |
| `OUT_OF_SCOPE_VENDOR` | 20 | `public/mathjax/tex-svg.js` 第三方压缩发行版，非本仓代码 |
| `FP_SCANNER_SYMBOL` | 24 | 跨文件同名符号碰撞，详见 §4.1 |
| `FP_ENTRY_SUMMARY` | 26 | “X 是 … 入口”“main 经 N 跳到达 …”是调用链摘要，不是独立 sink |
| `FP_FIXED_PATH` | 9 | 写入路径为仓库内固定常量（如 `RESULTS/align-zh.jsonl`） |
| `FP_FIXED_HOST` | 6 | 请求目标固定（termonline / youdao / lobid / Wikidata），查询词已 URL 编码 |
| `FP_DEAD_CODE` | 1 | `compose_from_ledger.py` 文件头明示已废弃、勿再执行 |
| `FP_NON_SECURITY_RANDOM` | 1 | `random.sample(rows, 30)` 用于抽样复现，不生成令牌 |
| `ACCEPTED_TRUSTED_PATH` | 165 | 本机 CLI 工具的路径来自仓库 slug/条目或操作者参数；无服务端权限边界 |
| `FIXED_FETCH_ALLOWLIST` | 1 | `tools/fetch.py` 已加白名单 |
| `FIXED_SCHEME_CHECK` | 2 | `tools/en_source_audit.py` 已加协议过滤 |
| `FIXED_PATH_CONTAINMENT` | 2 | `tools/fetch_entry.py` 已加包含性校验 |
| 合计 | 2353 | `NEEDS_MANUAL=0` |

## 4 误报与接受项分析

### 4.1 跨文件同名符号碰撞（24 条，扫描器缺陷）

典型消息：`不可信数据“命令行参数”流入 open() → 污点链：open(sink:sql-injection)（定义于 4.1.5_0/background.js）`。

原因：扫描器把 Python 内置 `open` 与 `script/tmp/probe` 下 Chrome 扩展 `background.js` 中的同名 `open` 当作同一符号，构造出“Python 文件写入 → SQL 执行”的跨文件链。Python 的 `open()` 不执行 SQL，链不成立。

受影响文件包括 `tools/compose_from_ledger.py`、`tools/progress.py`、`tools/termonline_token.py`、多个 `specs/021` 脚本。全部 24 条归为 `FP_SCANNER_SYMBOL`，不修代码。

### 4.2 入口/调用链摘要（26 条）

`main 是 path-traversal 入口`、`check_ledger 是 path-traversal 入口`、`main 经 1 跳到达 path-traversal` 等，是把“命令行参数进入某个函数”标成 sink 的摘要，不是某一行真的执行了危险操作。对应 sink 行在 `路径穿越` 类别中另行判定。

### 4.3 路径穿越（177 条 tracked）

| 子类 | 条数 | 处置 |
| ---- | ----: | ---- |
| 操作者 CLI 路径 / 仓库 slug | 165 | 接受：本机工具无服务端权限边界 |
| 仓库内固定常量 | 9 | 误报 |
| 上游 HTML 资产路径 | 2 | 已修（`fetch_entry.py` 包含性校验） |
| 废弃工具 | 1 | 误报（死代码） |

代表例：

* `tools/divergence.py` 把三方合并冲突写成 `state/` 下 `.html` 快照；`slug` 来自 `baseline/en-errata/divergences.json`，`out` 为固定 state 目录，非外部输入。
* `tools/rebuild_dir.py` 写 `zh/SUMMARY.md`、`zh/mu-lu-s.md`；目标名是仓库内固定文件名。
* `tools/check_terms.py --check-ledger <path>`、`tools/progress.py --out <path>`、`tools/check_images.py --out <path>`：参数由维护者在本机输入，属工具契约而非攻击面。
* `specs/021`、`specs/060` 等一次性脚本：路径为 `RESULTS` 常量或 slug，运行环境是本机维护者。

**真正需要修的是上游数据进入落盘路径**：`fetch_entry.save(relpath)` 的 `relpath` 来自 SEP HTML 的图片/补充材料相对路径；`fetch_audit` 的资产名同理。已改为 `contained_path(edir, relpath)`，越界抛 `ValueError`，不会静默写到 `html/<slug>/` 外。

### 4.4 SSRF（9 条 tracked）

| 文件 | 目标 | 处置 |
| ---- | ---- | ---- |
| `tools/cnki_query.py` | `api.termonline.cn` / `dict.youdao.com` | 固定主机；查询词 `urllib.parse.quote` |
| `tools/tl_jwt_crawl.py` | `api.termonline.cn` | 固定 API；JWT 走 TLS（本轮修复校验） |
| `specs/058/.../wikidata_person_sweep.py` | `www.wikidata.org` | 固定 base；参数 `urlencode` |
| `tools/fetch.py` | `plato.stanford.edu` | 已加协议/主机白名单 + 重定向逐跳校验 |
| `tools/en_source_audit.py` | 条目引用的外部链接 | 链接检查器设计如此；已加 http/https 过滤 |

`tools/fetch.py` 的白名单同时覆盖首跳与重定向：`_SafeRedirect.redirect_request` 在跟随前再次 `_validate_url`，避免“首跳合法、二跳内网”。实测 `https://plato.stanford.edu/contents.html` 与 `http→https` 重定向均返回 200。

### 4.5 不安全随机（1 条）

`specs/058/.../sample_recheck_b34.py` 用 `random.sample(rows, 30)` 复现抽样；不用于密码、令牌、会话 ID。归为 `FP_NON_SECURITY_RANDOM`。

### 4.6 本地未跟踪面（2096 条）

| 目录 | 条数 | 性质 |
| ---- | ----: | ---- |
| `script/`（非 tmp） | 1104 | 一次性草稿脚本，gitignore |
| `script/tmp/probe` | 940 | Chrome 探针用户目录内的第三方扩展（含 minified bundle） |
| `state/` | 52 | 本地运行态脚本/实验 |

这些文件不进入仓库、不进入 CI、不随 PR 分发。它们包含少量真实的本地危险模式（如 `script/_edw_fill.py` 的 `exec` 代码注入、`script/conv_quotes_cosmopolitanism.py` 的命令拼接），但攻击面仅限本机维护者。建议清理 `script/tmp/probe`，复用一次性脚本前单独审读；本 PR 不删除本地文件。

### 4.7 第三方 MathJax（20 条）

`public/mathjax/tex-svg.js` 是 MathJax 发行版压缩文件（单行 minified），扫描器对其报出 `command-injection`、`xss`、`ssrf`、`mongo-sort-injection` 等启发式命中。第三方构建产物，不在本仓维护范围；升级 MathJax 版本时随上游处理。

## 5 扫描器之外的补充审计

### 5.1 TLS 校验关闭（3 处，已修）

| 文件 | 主机 | 修复前 | 实测 |
| ---- | ---- | ---- | ---- |
| `tools/tl_jwt_crawl.py` | `api.termonline.cn` | `check_hostname=False`、`CERT_NONE` | 默认上下文 200，cert verify ok |
| `specs/013/.../gnd_batch_candidates.py` | `lobid.org` | 同上 | 默认上下文 200 |
| `specs/058/.../backfill_auto.py` | `www.wikidata.org`（本地代理 127.0.0.1:7890） | 同上 | 代理 + 默认上下文 200 |

`tl_jwt_crawl.py` 的请求头带 `X-Access-Token`；关闭校验等于把 JWT 暴露给任何能劫持 TLS 的中间人。三处均恢复 `ssl.create_default_context()`。

### 5.2 已提交 JWT 与 PII（开放项，需用户执行）

`specs/008-terminology-campaign/results/queries/termonline-all/belief.json` 的 `raw` 字段保留了一次 401 响应，其中含：

* 一枚 JWT，`exp=2026-12-25`（尚未到期）；服务端响应文本为“token非法无效”，说明该令牌已被拒绝；
* `username` 字段形似中国大陆手机号。

风险：公开仓库可被任意人读取；虽然令牌已被服务端拒绝，仍应按“已泄露”处置。本 PR 的处理：

1. 新增 `tools/cnki_query.py::redact_secrets()`，未来 `note/error/raw` 落盘前脱敏 JWT 与 `token=`，并有回归测试。
2. 不修改既有证据文件、不重写 git 历史：公开 PR 的 diff 会再次展示旧值，且项目禁止 force push；历史清理须单独裁定。
3. **请用户立即在术语在线重新登录，使该会话失效；如认为必要，另行评估 `git filter-repo` + 协调所有克隆的清理方案。**

### 5.3 git 历史密钥检索（补偿）

`mimosa git-secrets` 返回 `git-log-failed:unknown`、`commitsScanned=0`，属工具本机失败。补偿检索：

* `git log --all -S` 检索 `ghp_`、`github_pat_`、`BEGIN RSA PRIVATE KEY`、`BEGIN OPENSSH PRIVATE KEY`：无命中。
* `AKIA`：命中两个“原始物入库”提交，内容为图片/二进制资产，属 base64 偶然串，非 AWS 密钥。
* `X-Access-Token`：命中爬虫代码提交，属代码关键字。
* 工作树（排除 `.secrets/`）正则检索常见密钥格式：无命中；`.secrets/` 从未入库（`git log -- .secrets` 为空）。

局限：`-S` 只覆盖指定模式，不等价于全历史熵扫描。建议在干净克隆或 CI 复跑 `mimosa git-secrets`。

### 5.4 VitePress 补扫（2 条）

| 文件:行 | 规则 | 判定 |
| ---- | ---- | ---- |
| `.vitepress/math-plugin.mjs:90` | `replaceAll` 转义不完整（INFO） | `all.replaceAll('<','&lt;')` 只处理 `<`；已足以阻断标签注入，`>` 单独无攻击性。接受 |
| `.vitepress/merge-shards.mjs:43` | `Object.assign` 原型污染（WARNING） | 输入是 VitePress 分片构建产物 `hashmap.json`，构建产物可信；能改 dist 的人已能改站点。接受 |

另：`.vitepress/config.mts` dev server `host: '0.0.0.0'`。仅本地 dev 生效，方便局域网预览；如不需要，建议改 `127.0.0.1`。记录不修。

### 5.5 CI 注入与供应链（已修）

* `format.yml` 在 `pull_request` 上把 `steps.changed.outputs.all_changed_files` 直接插值进 `run`，并在 lint 步骤把文件列表裸插值给 `bunx`。PR 文件名可由外部贡献者控制，`"`、`$()`、反引号可逃逸。已改为 `env` 传值 + 多行 output + 文件列表 `xargs -d '\n'`。
* `create-pdf.yml` 把 `inputs.letters` 插值进 Python 源码；已改为 `env` + `os.environ`。
* 25 处 `actions/checkout@v7`、`actions/setup-python@v7`、`actions/upload-artifact@v7`、`github/codeql-action/{init,analyze}@v4` 已钉到 40 位 commit SHA；其余第三方 Action 原本已钉版。
* 复核：`delivery-check` 从 25 条 medium 降到 **0**；9 个工作流 YAML 语法校验通过。

### 5.6 其他 Mimosa 检查

| 检查 | 结果 | 处置 |
| ---- | ---- | ---- |
| `agent-check` | 10 个 Agent 指令/MCP/工作流文件，无风险 | 无需处理 |
| `release-check` | `public/` 3 个文件，无泄露 | 无需处理 |
| `license-check` | 0 个 package.json 依赖（锁文件不入库），无风险 | 无需处理 |
| `supply-chain-check` | 2 条 low，均在 `state/mathval/package.json`（本地未跟踪实验） | 不入库，无需处理 |
| `pii-check` | 422 条，全部在 `.vitepress/dist-*`（gitignore 派生物） | 见下 |
| `semgrep .vitepress` | 21 文件，2 条 INFO/WARNING | §5.4 |

`pii-check` 的 422 条全部命中构建产物：414 条“信用卡号”实为 Unix 毫秒时间戳（13 位且偶然通过 Luhn）、archive.org 标识、ISBN/DOI 片段、SHA-256 十六进制片段；8 条“SSN”实为 `978-981-15-4847-5` 一类 ISBN/DOI 的子串。逐文件上下文复核未发现真实卡号或 SSN。该检查 `coverage.truncated=true`（5000 文件上限），结论只覆盖已扫描文件。

## 6 修复的验证

| 验证 | 命令 | 结果 |
| ---- | ---- | ---- |
| 全量门禁 | `python tools/check_all.py` | 24 项，失败 0 |
| 新增安全回归 | `python -m unittest tools.tests.test_security_hardening` | 7/7 OK |
| 受影响模块 | `python -m unittest tools.tests.test_fetch_entry ...` | 64 项 OK（skip 2） |
| 白名单实测 | `fetch.get(https://plato.stanford.edu/contents.html)` | 200，307144 字节 |
| 重定向实测 | `fetch.get(http://plato.stanford.edu/contents.html)` | 200，307144 字节 |
| 拒绝实测 | `file://`、`127.0.0.1`、`evil.example`、`ftp://` | 全部 `FetchError` |
| 包含性实测 | `contained_path(base, '../x')` 等 | 全部 `ValueError` |
| 脱敏实测 | 裸 JWT / `token=` | 均替换为 `[REDACTED…]` |
| 封印复算 | 三件 SHA-256 | 全部一致 |
| 交付链 | `mimosa delivery-check` | 0 项 |

## 7 局限与不作断言

1. 扫描器 `runStatus=inconclusive`，`validation.investigated=0`；全部 finding 是静态候选。本报告不声称“无漏洞”。
2. 未执行目标项目的网络服务或运行时利用验证；`evidenceBoundary=static_only_no_runtime_execution`。
3. 9547 个 `.html` 未扫描（用户要求），其中若有内联脚本风险不在本报告覆盖内。
4. 本地未跟踪件只做分组归因，未逐条人工复核 2096 条；它们不进入分发面。
5. `mimosa git-secrets` 失败、`pii-check` 截断，均已在对应节标明。
6. 依赖摘要仅覆盖 143 个可识别包；`node_modules` 与壳仓依赖不在本仓锁文件内。

## 8 开放行动（需用户/后续会话）

| 优先级 | 行动 | 理由 |
| ---- | ---- | ---- |
| 高 | 术语在线重新登录，使已提交 JWT 会话失效 | 令牌在公开历史中，exp 2026-12-25 |
| 中 | 评估历史清理（filter-repo + 全克隆协调）或接受现状 | 本 PR 不 force push |
| 中 | 在干净克隆/CI 复跑 `mimosa git-secrets` | 本机 0 commits |
| 低 | 清理 `script/tmp/probe` Chrome 用户目录 | 940 条第三方扩展 finding，纯本地噪声 |
| 低 | 如需收窄本机暴露，`.vitepress` dev server 改绑 `127.0.0.1` | 当前 `0.0.0.0` 仅 dev |
| 低 | 未来抓取目标超出 `plato.stanford.edu` 时同步改白名单 | 否则抓取显式失败 |

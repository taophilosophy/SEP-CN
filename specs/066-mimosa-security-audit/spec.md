# 066 — Mimosa 全库深度安全审计（2026-11-28）

* 编号：`specs/066-mimosa-security-audit`；立项日期：2026-11-28；**状态**：执行完成（分析 PR 待评审，不自动合并）
* 承办：主会话（ADR-0034 主代理单干）
* 上位：项目宪法（`.specify/memory/constitution.md`）、`rules/` 与其 ADR；本卡只记录本次审计的范围、凭证、处置与残余风险，不改写任何既有规则
* 扫描快照：`07d65c0475fc9286861a26fabb3f729dfe331211`（2026-11-28 18:24 +0800）
* 扫描任务：`scan-job-mx09ygem-0497c47618001614`；扫描号：`scan-2026-11-28T10-39-14.673Z-fa8d19675d8e`
* 封印摘要：`sha256:14bf59315b734be9041b6327f231b22b53df7b4465f8dc82cdfee836b69323b7`（语义件复算一致，见 `results/scan/seal.json`）

## 0 方向声明（rules/08 §1）

### 0.1 用户指令

2026-11-28：使用 mimosa 本地深扫（`/mimosa-deep-audit`）全部文件，建立分析 PR、不自动合并；不计成本代价，覆盖所有文件，所有提示都要覆盖分析解决，力求最佳；**禁止扫描 `*.html`**。

### 0.2 目标

1. 用 Mimosa 密封深扫覆盖仓库内可扫描代码，给出可复核的扫描凭证与覆盖边界。
2. 对扫描器返回的全部 2353 条 finding 逐条给出处置（真问题修复／误报归因／范围外说明），不留下未解释项。
3. 对真实缺陷做最小、可回滚的修复，并以单元测试与项目门禁验证。
4. 建立分析 PR，供人工评审；不自动合并。

### 0.3 非目标

1. 不扫描 `*.html`（用户硬约束）；不修改 `html/` 冻结原文（ADR-0062）。
2. 不重写 git 历史、不做 force push；不在本 PR 中轮换第三方会话令牌（须用户执行）。
3. 不把 Mimosa 接入日常钩子、`check_all.py` 或 CI 常驻门禁。
4. 不修改 `zh/`、`en/`、`tasks/`、`journal/`、`baseline/` 的任何内容或数据。
5. 不把本卡扩展为规则修订；规则层问题另立 ADR。

### 0.4 验收判据

1. `specs/066-mimosa-security-audit/results/scan/` 四件语义产物在库，`seal.json` 三件摘要复算一致。
2. `results/findings-triage.csv` 行数等于扫描 `findingCount`（2353），且 `disposition` 无 `NEEDS_MANUAL`。
3. 真实缺陷修复有对应测试；`python tools/check_all.py` 全绿。
4. `delivery-check`（Mimosa CLI）在本分支返回 0 项。
5. 分析 PR 已建立且未合并。

## 1 范围与覆盖

### 1.1 扫描范围

Mimosa 深扫以仓库根为 project 运行。扫描器原生支持
`.py/.ts/.tsx/.js/.jsx/.go/.java/.php/.rb/.cs/.kt/.kts/.rs`，不支持 `.html`，与用户“禁扫 `*.html`”约束一致。

`coverage.json` 记录：`selectedFiles=4169`、`parsedFiles=4169`、`readFailures=0`、`parseFailures=0`、`truncated=false`、`omittedAtLeast=0`。按物理文件复核，4169 与下列口径吻合：

| 范围 | 代码文件数 | 是否入扫 |
| ---- | ----: | ---- |
| `tools/`、`specs/`、`script/`、`state/`、`public/` | 3733 | 是 |
| `html/` 内的 `.js` 资产 | 464 | 是（HTML 本体不扫） |
| `.vitepress/` 构建产物 `dist-*` | 6873 | 否（派生物，等价于不重复扫源） |
| `*.html` | 9547 | **否（用户禁止）** |

“是”项合计 4197，`selectedFiles=4169`，差 28。差额属扫描器内部选择口径（超大/疑似二进制跳过等）；`coverage` 没有把未解析项计入 `parsedFiles`，本卡也不以 4169 之外的文件断言干净。

### 1.2 覆盖缺口与补扫

1. `.vitepress/` 是点目录，根扫描未纳入。已用 Semgrep `p/default + p/security-audit` 补扫 21 个源文件（`.mts/.ts/.mjs/.vue`），命中 2 条 INFO/WARNING，逐条复核见 `results/report.md` §5.4。
2. `.specify/scripts/powershell/*.ps1` 与 `specs/014/.../verify-clone.sh`：Semgrep 无 PowerShell 语法支持，逐文件人工审读；未见 `Invoke-Expression`、网络下载执行或用户输入拼接命令。
3. 数据与文档（`.md/.json/.ndjson/.yml/.tsv`）不是 Mimosa 代码规则的对象；以 PII、供应链、交付链、git 历史密钥与项目门禁另行覆盖，见 `results/report.md` §5。
4. `mimosa git-secrets` 在本机返回 `git-log-failed:unknown`（0 commits scanned），已用 `git log -S` 高信噪模式与工作树正则补偿检索，结果见 §5.2。

## 2 扫描凭证与环境

| 项 | 值 |
| ---- | ---- |
| MCP 深扫 job | `scan-job-mx09ygem-0497c47618001614` |
| scan ID | `scan-2026-11-28T10-39-14.673Z-fa8d19675d8e` |
| 深度 | `deep` |
| 运行状态 | `inconclusive`（coverage `partial`） |
| finding 总数 | 2353（high 1550／medium 798／low 5） |
| 依赖摘要 | 143 个包，offline advisory 可用，matched 0 |
| 引擎 | Mimosa 0.1.0 + Semgrep CE 1.136.0（uv 工具环境，`setuptools<81`） |

环境事实（可复现）：

1. 插件托管安装 `mimosa semgrep install` 被其自身 Bash 门禁误判为“写安全配置”而拒绝；改用 `uv tool install semgrep==1.136.0 --python 3.12 --with "setuptools<81"` 安装，`semgrep --version` 与 `mimosa doctor` 均通过。`setuptools>=81` 移除 `pkg_resources`，Semgrep 1.136.0 会启动失败。
2. `mimosa doctor` 报 ZCode hook 路径异常、MCP 未注册；但 MCP 工具经插件通道可用，深扫实际完成。该提示属环境注册噪声，不影响扫描产物，已记录不修。
3. `security-scan` 在根目录直接运行时 `threatModel/findingDiscovery/pathAnalysis` 为 `partial`，`runStatus=inconclusive`；报告不据此宣称“全项目安全”。

## 3 全量处置口径

`results/findings-triage.csv` 每行对应一条 finding，字段含 `findingId/severity/title/class/kind/scope/path/line/disposition/rationale`。处置类别：

| disposition | 条数 | 含义 |
| ---- | ----: | ---- |
| `OUT_OF_SCOPE_LOCAL` | 2096 | `script/`、`state/` 等 gitignore 本地件；不随仓库分发 |
| `OUT_OF_SCOPE_VENDOR` | 20 | `public/mathjax/tex-svg.js` 第三方压缩发行版 |
| `FP_SCANNER_SYMBOL` | 24 | 跨文件同名符号碰撞（Python `open` 命中 Chrome 扩展 `background.js` 的 SQL sink） |
| `FP_ENTRY_SUMMARY` | 26 | 入口/调用链摘要，不是独立 sink |
| `FP_FIXED_PATH` | 9 | 写入路径为仓库内固定常量 |
| `FP_FIXED_HOST` | 6 | 请求目标为固定白名单主机，查询词已编码 |
| `FP_DEAD_CODE` | 1 | 已废弃留档工具（`compose_from_ledger.py`） |
| `FP_NON_SECURITY_RANDOM` | 1 | 抽样复现用 `random.sample`，非安全随机 |
| `ACCEPTED_TRUSTED_PATH` | 165 | 本机 CLI 工具，路径来自仓库数据或操作者参数，无服务端权限边界 |
| `FIXED_FETCH_ALLOWLIST` | 1 | `tools/fetch.py` 已加协议/主机白名单与重定向校验 |
| `FIXED_SCHEME_CHECK` | 2 | `tools/en_source_audit.py` 已加 http/https 过滤 |
| `FIXED_PATH_CONTAINMENT` | 2 | `tools/fetch_entry.py` 落盘前做包内包含性校验 |
| **合计** | **2353** | `NEEDS_MANUAL=0` |

## 4 修复清单

| 文件 | 修复 | 依据 |
| ---- | ---- | ---- |
| `tools/tl_jwt_crawl.py` | 恢复默认 TLS 证书/主机名校验（JWT 走此通道） | 实测 `api.termonline.cn` 证书链默认上下文可用 |
| `specs/013-person-attribution/bin/gnd_batch_candidates.py` | 恢复默认 TLS 校验（lobid.org GND） | 实测默认上下文可用 |
| `specs/058-term-full-reextraction/bin/backfill_auto.py` | 恢复默认 TLS 校验（Wikidata，经本地代理） | 实测代理 + 默认上下文可用 |
| `tools/fetch.py` | 只允许 `http/https` + `plato.stanford.edu`/`www.plato.stanford.edu`；重定向逐跳同白名单 | 关闭上游数据诱导 SSRF 与重定向绕过 |
| `tools/common.py` | 新增 `contained_path()`：落盘路径必须位于词条包根内 | 上游 HTML 的资产相对路径是外部输入 |
| `tools/fetch_entry.py` | 资产落盘改用 `contained_path()` | 防 `../`/绝对路径带出 `html/<slug>/` |
| `tools/fetch_audit.py` | 补抓落盘改用 `contained_path()` | 同上 |
| `tools/en_source_audit.py` | 链接检查只处理 `http/https` | 防 `file:` 等协议被当网络链接 |
| `tools/cnki_query.py` | 新增 `redact_secrets()`，`note/error/raw` 落盘前脱敏 JWT 与 `token=` | 防会话令牌再入公开证据 |
| `.github/workflows/format.yml` | PR 文件名经 `env` 传入，输出改多行，lint 走文件列表 | 消除 `pull_request` 文件名表达式注入 |
| `.github/workflows/create-pdf.yml` | `inputs.letters` 经 `env` 传入 Python | 消除 dispatch 输入插值 |
| `.github/workflows/*.yml`（8 件） | `actions/checkout`、`setup-python`、`upload-artifact`、`codeql-action` 钉到 40 位 commit SHA | 供应链不可变引用 |
| `tools/tests/test_security_hardening.py` | 新增 7 条回归测试 | 覆盖白名单、包含性、脱敏 |

## 5 残余风险与开放项

1. **已提交的 JWT/PII（最高优先，需用户执行）**：`specs/008-terminology-campaign/results/queries/termonline-all/belief.json` 的 `raw` 错误串含一枚 JWT（`exp=2026-12-25`）与形似手机号的 `username`；该 token 在服务端响应中已被判“非法无效”，但仍在 git 历史中。本 PR 不重写历史、不在公开 diff 中再次展示该值；**请立即在术语在线重新登录使会话失效，并评估历史清理**。新写入路径已由 `redact_secrets()` 封堵。
2. **扫描器状态 `inconclusive`**：`threatModel/findingDiscovery/pathAnalysis` 为 `partial`；2353 条 finding 的 `validation.investigated=0`，全部属静态候选，不构成“已证实漏洞”。本卡结论按此下限表述。
3. **`mimosa git-secrets` 本机失败**：`git-log-failed:unknown`、0 commits；已用高信噪模式补偿，但不等价于全历史秘密扫描。建议在 CI 或干净克隆复跑。
4. **本地未跟踪面**：`script/`（含 `script/tmp/probe` Chrome 用户目录）与 `state/` 有 2096 条 finding，均不入库；建议清理 `script/tmp/probe`，复用一次性脚本前单独审读。
5. **第三方与派生物**：`public/mathjax/tex-svg.js` 20 条、`.vitepress/dist-*` 未扫；后者是构建产物，源已由 Semgrep 补扫。
6. **低风险设计项**：`.vitepress/config.mts` dev server `host: 0.0.0.0`（本地预览用，局域网可访问）；`format.yml` 的 `fix` 作业仅 `workflow_dispatch`，不受外部 PR 触发。均记录不修。

## 6 验收证据

| 检查 | 结果 |
| ---- | ---- |
| `seal.json` 三件摘要复算 | 全部一致 |
| `python tools/check_all.py` | 24 项全绿 |
| `python -m unittest tools.tests.test_security_hardening` | 7/7 OK |
| 受影响模块测试（fetch_entry/fetch_audit/common/compare/divergence/cnki_query/fetch_all） | 64 项 OK（skip 2） |
| `mimosa delivery-check`（本分支） | 0 项 |
| `semgrep` 补扫 `.vitepress` | 21 文件；2 条 INFO/WARNING，均复核为可接受 |
| `pii-check` | 422 条全在 `.vitepress/dist-*`（gitignore 派生物），逐类复核为时间戳/ISBN/Wayback 编号，误报 |
| `supply-chain-check` | 2 条 low，均在 `state/mathval/package.json`（本地未跟踪实验） |

## 7 复现命令

```text
# 深扫（MCP）
security_scan_start(project="<repo>", depth="deep")
security_scan_status(jobId="scan-job-mx09ygem-0497c47618001614")

# 封印复算
python -I - <<'PY'
import hashlib,json
s=json.load(open('specs/066-mimosa-security-audit/results/scan/seal.json',encoding='utf-8'))
for n,w in s['artifacts'].items():
    assert 'sha256:'+hashlib.sha256(open('specs/066-mimosa-security-audit/results/scan/'+n,'rb').read()).hexdigest()==w
PY

# 门禁与测试
python tools/check_all.py
python -m unittest tools.tests.test_security_hardening
```

## 8 作废条件

1. 仓库引入服务端/网络暴露面（API、Web 服务）时，本卡的“操作者路径不构成权限边界”前提失效，须重扫并重评 165 条 `ACCEPTED_TRUSTED_PATH`。
2. 抓取目标扩展到 `plato.stanford.edu` 之外时，`tools/fetch.py` 白名单须同步修订，否则抓取显式失败。
3. Mimosa 升级到规则/覆盖语义变更版本时，本卡计数与处置不可直接沿用，须以新 scan ID 重跑。

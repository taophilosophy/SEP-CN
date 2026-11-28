# 安全策略 Security Policy

## 支持范围

本仓库是《斯坦福哲学百科全书》（SEP）词条简体中文翻译与工具链仓库，不发布可执行服务或库。安全维护覆盖：

- `tools/`、`specs/*/bin/` 下的脚本；
- `.github/workflows/` 中的 GitHub Actions；
- 抓取、转换与校对流程中的凭据处理。

翻译正文与 `baseline/` 数据不属于可执行面，但数据泄露、供应链或 Actions 权限问题仍按本策略报告。

## 报告漏洞

请使用 GitHub 的私密漏洞报告：仓库 **Security → Report a vulnerability**。

- 不要开公开 issue，不要在报告中附带可利用细节、访问令牌或个人信息。
- 报告请包含：受影响文件与提交、复现步骤、影响范围、建议修复。
- 维护者会尽快确认；修复后可在报告中致谢（如你愿意）。

## 凭据与数据

- 仓库不存储令牌、密码或私钥；Actions 使用 `GITHUB_TOKEN` 与仓库 secrets。
- 脚本的中间产物写入本地运行态目录（`state/`），不入库。
- 翻译流程不收集终端用户数据。

## CodeQL 误报登记

`py/clear-text-storage-sensitive-data` @ `specs/013-person-attribution/bin/gnd_triage.py`：

- GND（Gemeinsame Normdatei）是德国国家图书馆的公开规范档；脚本只把公开的出生／死亡**年份**写入公开台账 `specs/013-person-attribution/results/`。
- 不写入完整生日、地址、联系方式或其他个人数据，也不涉及凭据。
- CodeQL 将公开规范档的 `dateOfBirth` 视为 private。项目 2026-11-27 裁定为误报；2026-11-28 在 GitHub code scanning 以 **false positive** 关闭（alert #24）。不引入加密或哈希，以免破坏台账的可读性与可复核性。

## CodeQL 告警处置与威胁模型（2026-11-28）

本仓库不是可执行服务：`tools/` 与 `specs/*/bin/` 是维护者在本地或 CI 中显式运行的翻译流水线脚本，输入来自操作者命令行参数、仓库内受信文本与固定的上游站点。按此威胁模型对全部开启告警分类处置：

| 类别 | 处置 | 依据 |
| ---- | ---- | ---- |
| `actions/unpinned-tag`（9） | **修复**：第三方 action 全部改为固定提交 SHA | 供应链完整性；标签可被移动 |
| `py/regex-injection`（动态 tag／name 共 8 处） | **修复**：`re.escape()` 转义后拼入模式；余 3 处为 `rules/naming.json` 登记表配置正则，驳回（won't fix） | 阻断正则元字符注入；配置即模式属设计行为 |
| `py/xml-bomb`（1） | **加固**：feed 解析前拒绝 `<!DOCTYPE`／`<!ENTITY`；余告警按误报关闭 | 阻断实体膨胀与外部实体 |
| `py/polynomial-redos`（408） | 驳回（won't fix）：本地／CI 对仓库内受信文本运行，输入规模与运行时限受控 | 无可被外部租户触发的服务端入口 |
| `py/path-injection`（396） | 驳回（won't fix）：CLI 操作者显式指定的仓库内路径，本地读写即工具功能 | 不以服务形式暴露 |
| `py/partial-ssrf`（6）、`py/full-ssrf`（1） | 驳回（won't fix）：抓取工具按操作者给定或固定上游 URL 请求 | 本地运行，非多租户服务 |
| `py/command-line-injection`（1） | 驳回（false positive）：`subprocess.run(list)` 不经 shell | 参数不参与 shell 解析 |
| `js/path-injection`（10）、`js/file-access-to-http`（1）、`js/remote-property-injection`（1） | 驳回（won't fix）：`specs/` 下一次性分析／截图脚本，参数由操作者提供 | 非站点运行时 |

上述驳回均在对应告警内附同口径说明；若仓库未来对外提供网络服务或接受不可信输入，须重新评估并重开相关告警。2026-11-28 处置后，code scanning 开启告警为 0：本批固定第三方 action 9 条、转义动态正则 8 条，其余按上表逐类驳回并留说明。

## 供应链

- GitHub Actions 的第三方 action 一律固定到提交 SHA（标签仅作注释），官方 action 按最小必要权限配置。
- CodeQL 采用 advanced setup（`.github/workflows/codeql.yml`）：`python`／`javascript-typescript`／`actions` 三语言，`security-extended` 查询套件，push、PR 与每周一 02:23 UTC 扫描；默认设置已停用。
- 发现可疑提交、依赖或工作流权限变更，请按“报告漏洞”一节私密报告。

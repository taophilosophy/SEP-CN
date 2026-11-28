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

## 供应链

- GitHub Actions 使用官方 action，权限按最小必要配置。
- 发现可疑提交、依赖或工作流权限变更，请按“报告漏洞”一节私密报告。

# Tasks

- [x] Task 1: 新增理论文档 `rules/reference/engineering-doctrine/00b-zhinan-xingyi.md`
  - [x] SubTask 1.1: 来源核对——从 `00a-yike-source.md` §2（第十七 历史存在论、二十一 革命与改革）、§3（补充总纲 31 重要决策）与 `00-philosophy.md` §3（六问）、§6（0 信任）、§8（工程推论）提取依据，逐条标注条目编号；明示“知难行易”为项目侧提炼，不写成源文原文
  - [x] SubTask 1.2: 撰写正文——知/行分层定义；四条命题（方向错误放大损失、手段可替换、知是前提而非替代、形式主义手段表演）；开工四问；六类反模式；方向声明卡模板；与 rules/04、rules/06、doctrine 02 的关系；失效条件与复审触发
  - [x] SubTask 1.3: 更新 `rules/reference/engineering-doctrine/README.md` 目录表（00b 行）与 `NOTICE.md` 变更记录（2026-10-29 行）
  - [x] SubTask 1.4: 体例自检——不超过 1000 行/100KB；中文引号仅 “”‘’，无直角引号（U+300C–U+300F）；UTF-8 无 BOM、LF

- [x] Task 2: 新增约束性规则 `rules/08-intent-first.md`（H1：任务意图与方向先行（知难行易））
  - [x] SubTask 2.1: 适用范围与七条条文——方向声明、先问不猜、手段后置可替换、以验收判据验收、可逆快行/不可逆先知后行、知—行闭环、收工形式主义自检
  - [x] SubTask 2.2: 判例三条（含糊指令“优化一下” / 理论新增类指令 / 翻译任务起步）与 `rules/04`、`rules/06` 的衔接段
  - [x] SubTask 2.3: 体例自检——不超过 300 行/30KB（`tools/check_doc_size.py`）；中文引号与换行合规；引用的理论条款编号与 00b 一致

- [x] Task 3: 新增 ADR 并登记索引
  - [x] SubTask 3.1: `rules/adr/0018-知难行易全局规则.md`——背景、决策（宪法 v1.2.0 新增 VII 条 + 00b + rules/08 + 索引同步）、后果（正面/代价/失效条件）、复审触发（2027-01-21，与 specs/004 同期）
  - [x] SubTask 3.2: `rules/adr/README.md` 索引表追加 0018 行（并补登既有 0017 行）

- [x] Task 4: 修订宪法 v1.2.0
  - [x] SubTask 4.1: `.specify/memory/constitution.md` 追加 `### VII. 知难行易（先明方向，后择手段）`：方向/目标/非目标/验收判据/代价承担者先于手段；手段可替换；含糊先问不猜；完成以验收判据与证据判定；可逆快行、不可逆先知后行；指向 rules/08；I–VI 编号与内容不动
  - [x] SubTask 4.2: 版本行改为 `**Version**: 1.2.0 | **Ratified**: 2026-10-26 | **Last Amended**: 2026-10-29`
  - [x] SubTask 4.3: 提交信息注明“修订宪法 v1.2.0”并说明理由（已提交 52c0ef56）

- [x] Task 5: 全局入口与索引同步
  - [x] SubTask 5.1: `rules/README.md`——规范层级第 1 条改“七项核心原则”并列出知难行易；规则索引表新增 08 行；规则地图“约束性规则”改 `rules/01-08`；快速判例新增“新任务或需求含糊 → 先写方向声明再动手”
  - [x] SubTask 5.2: `rules/06-governance.md` 首句“宪法六原则”改为“宪法七原则”，新增“任务方向声明（宪法 VII 落地）”节与验收判据条款
  - [x] SubTask 5.3: `README.md`、`CONTRIBUTING.md` 的“六项核心原则”改为“七项核心原则”（历史 `RELEASE-NOTES.md`、ADR-0016 不改写）
  - [x] SubTask 5.4: `AGENTS.md`——规范层级第 1 条原则列表补“知难行易”；开工五分钟新增第 0 步“方向确认”；硬约束速览新增“知难行易”条；按任务类型必读表新增“收到新指令/需求含糊 → rules/08”行
  - [x] SubTask 5.5: `specs/004-engineering-doctrine/spec.md` 复审记录追加 2026-10-29 一行
  - [x] SubTask 5.6: 同步全部任务入口——rules/01、02、03、04、05、07 各加方向先行条款；`tasks/README.md` 加任务方向声明；`specs/005`、`specs/008` 会话卡加开工前方向声明

- [x] Task 6: 验收与提交
  - [x] SubTask 6.1: `python tools/check_all.py` 七项全绿
  - [x] SubTask 6.2: 交叉核对——宪法版本与七条原则、rules/README 索引、规则地图、ADR 索引与磁盘文件一一对应；检索“六项核心原则/宪法六”仅历史文档命中；无死链、无占位符
  - [x] SubTask 6.3: 提交（中文一行信息，注明“修订宪法 v1.2.0”，只含本任务相关文件；提交 52c0ef56，22 个文件）

# Task Dependencies

- Task 2 依赖 Task 1（规则条文引用理论条款编号）
- Task 3 依赖 Task 2 与 Task 4 的条文内容
- Task 4 依赖 Task 2（宪法 VII 指向 rules/08）
- Task 5 依赖 Task 1、Task 2、Task 3、Task 4
- Task 6 依赖 Task 1—Task 5

# Quickstart: 端到端验证指南

**Feature**: specs/001-sep-sync-pipeline | **Date**: 2026-10-26

前置条件：Python 3.15+；网络可达 plato.stanford.edu；在本仓库根目录执行。

## 场景 1：词条包基线（对应 SC-001）

```sh
# 抓取 5 个结构迥异样本（重数学/逻辑符号/表格脚注/含图/纯文本）
python tools/fetch_entry.py set-theory logic-classical bayes-theorem bell-theorem quine

# 期望（stdout JSON）:
#   每词条 files 含 main；bayes-theorem 含 notes（kind=notes）；
#   set-theory 含 basic-set-theory.html（kind=supplement）；
#   bell-theorem 含 image1.jpg、image2.jpg（kind=image）；
#   全部文件 sha256 已登记，en/<slug>/ 下可找到原始 HTML

# 审计复算（宪法门 I）
python tools/baseline_audit.py
# 期望: hash_fail=[], missing_files=[]
```

## 场景 2：更新检测（对应 SC-002）

```sh
python tools/detect_updates.py --rss
# 期望: from_rss 含 2026-10 事件（如 kant-transcendental revised 2026-10-24、
#       academic-freedom new 2026-10-17），queue 标注 action

python tools/detect_updates.py --archinfo --only kant-transcendental
# 期望: from_archinfo 报出 baseline_edition 与 latest_edition 差异（若基线已建立）
```

## 场景 3：版本比较（对应 SC-003）

```sh
# 用存档旧版对在线新版做真实 diff（anaxagoras: winter2019 存档 vs 在线版差异巨大，效果直观）
python tools/compare_versions.py anaxagoras --old archives/winter2019 --new live
# 期望: items 为段落级变更清单，每条含 section（英文节号）与 excerpt_en；
#       zh_doc 指向 a/anaxagoras.md
```

## 场景 4：文档任务与三审三校（对应 SC-004）

```sh
python tools/task_ops.py create anaxagoras --kind retranslate
python tools/task_ops.py clear anaxagoras          # gate: baseline_audit 通过
python tools/task_ops.py advance anaxagoras --step draft --actor <名> --evidence <记录>
python tools/task_ops.py advance anaxagoras --step s1 --actor <名> --evidence <对照记录>
# ... 依次 s2 s3 r1 r2 r3
python tools/task_ops.py show anaxagoras
# 期望: state 与 steps 完整反映六道进度；跳步命令被拒绝（退出码 3）
```

## 场景 5：体例检查（宪法 VI）

```sh
python tools/check_style.py <中文 md>
# 期望: 弯引号/加粗空格/中西文空格/HTML 残留逐项报告；退出码语义见 contracts/cli.md
```

验收：五个场景全部符合期望注释即为通过；任何偏差记录进演示日志并回流修订流程文档（User Story 5）。

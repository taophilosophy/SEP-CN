# 斯坦福哲学百科全书简体中文版

[原版英文目录](https://plato.stanford.edu/contents.html)

[SEP 原版中文目录](SUMMARY.md)

[SEP 分类目录](mu-lu-s.md)

[开源地址](https://github.com/taophilosophy/SEP-CN)

<img src="./.gitbook/assets/wechat.png" width="25%" height="25%">

## 词条说明

* 凡是以 `*` 开头的且词条名中 **包含** `— see` 的词条都是指向其他词条的“别名词条”，例如 `*弗朗索瓦-马里‧阿鲁埃——见伏尔泰 Arouet, François-Marie — see Voltaire`，伏尔泰（Voltaire）是其笔名，“弗朗索瓦-马里‧阿鲁埃（François-Marie Arouet）”才是原名，但是实际上两个代表的是一个人。`*弗朗索瓦-马里‧阿鲁埃——见伏尔泰 Arouet, François-Marie — see Voltaire` 实际指向条目——`伏尔泰——Voltaire (J.B. Shank)`
* 凡是以 `*` 开头的且词条名中 **不包含** `— see` 的词条实际上是不存在的。例如 `*非洲哲学 African Philosophy` 实际上并不存在，仅作为母词条标题而出现。
* `*` 只代表当前的词条，不代表下辖的所有条目，凡是特殊词条都会一一标注。例如母词条 `*美学 aesthetics` 不代表美学下面的所有词条都是特殊词条，只有有 `*` 标注的才是特殊词条。
* `*超距作用——见量子力学：量子力学中的超距作用 action at a distance — see quantum mechanics: action at a distance in` 这个词条代表“超距作用”这个词条实际指向“量子力学”这个主目录下的 `量子力学中的超距作用` 这个词条。
* `递归——见递归 recursion — see recursion` 该词条实际不存在，经询问 SEP 编委会得知，该词条为一个梗。即点击后就知道什么是”递归“了。若要了解细节，请参考词条”递归函数“。

## 项目进度

全库处于**全量重译战役**期（FR-013）：既有机器翻译正文已清空，各词条正按"抓取基线 → 三审三校"状态机逐条重译。实时进度由 `python tools/progress.py` 生成，见 [PROGRESS.md](PROGRESS.md)（自动生成，不手改）。

## 关于 SEP

>斯坦福哲学百科全书由世界各地的哲学及相关学科的学者共同创建并维护，是一部不断更新的工具书。
>
>—— 联合主编：Edward N. Zalta 和 Uri Nodelman

## 项目治理

* [规则目录](rules/README.md) —— 仓库结构、编写体例、术语、翻译流程、CI 与软件工程治理
* [任务目录](tasks/README.md) —— 文档任务协议与三审三校状态机
* [工具目录](tools/README.md) —— 同步管线与目录校验脚本
* [工程规格](specs/001-sep-sync-pipeline/spec.md) —— 抓取、更新、比较、翻译管线
* [项目宪法](.specify/memory/constitution.md) —— 六项核心原则

## 许可证

本项目使用 BSD-2-Clause 许可证授权。

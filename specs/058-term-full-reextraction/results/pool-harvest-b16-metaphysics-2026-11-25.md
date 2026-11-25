# 收割批 16：形而上学与语言哲学族（2026-11-25）

用「含前缀的强归一」复核 75 个形而上学／心灵／语言哲学名（此前的纯相等比对会把带括注的键判成缺口，如 `haecceity；ecceitas（…）`、`supervenience（supervenient property…）`）。真缺 9 条。

## 登记 9 条

| 英文 | 主形 | 语料 | 说明 |
| ---- | ---- | ---- | ---- |
| fundamentality | 基础性 | 49 | 与 grounding 奠基、grounded 被奠基成族 |
| truthmaking | 使真 | 35 | 与 truthmaker 使真者、truthmaker theory 使真者理论分列 |
| identity over time | 历时同一性 | 20 | 与 numerical identity 数值同一、personal identity 人格同一性分列 |
| rigidity | 刚性（模态语境） | 25 | rigid designator 的抽象名词 |
| counterpart | 对应体（模态对应体理论） | 9 | Lewis |
| rigid designation | 严格指示（亦作“严格指示词”） | 4 | 克里普克 |
| extended mind | 延展心灵（与 extended cognition 延展认知分列） | 3 | 克拉克—查默斯 |
| sense and reference | 涵义与指称（亦作“意义与意谓”） | 2 | 弗雷格 Sinn und Bedeutung |
| deixis | 指示（语用学；与 demonstrative 指示词分列） | 265（指示） | 语用学 |

并入 1：`supervenience / supervenient`（原行译法括注已含 supervenient property，键补异形）。

## 不登与理由

* `change`、`event`、`process`、`disposition`、`powers`、`reference`：语料极高频但属**泛词**，登记会与各类复合词冲突（已有 change in meaning、process philosophy、dispositional belief 等行），不立基形。
* `conversational implicature`（已登记，会话含义／隐含）、`extended cognition`（已登记）、`numerical identity`（已登记）——本次候选的重合项。
* `illocutionary act`／`perlocutionary act`：语料仅 1–3 次（以言行事、语内），留待相关词条重译时再定形。

## 门禁

* 清单 `tasks/manifests/2026-11-25-058-batch67-terms.json`（9 行）；池 published=7
* 数据行 8,848→8,857；`registry_azsort` 守恒；`check_terms` 硬错误 0；告警 148／781 不变
* 无主形撞形告警

## 方法修正

批 15 的教训（建清单前先强归一）本轮执行；并进一步发现**纯相等比对不够**——键常带括注与异体说明，须用「任一 `/` 分段的强归一键**以候选为前缀**」判在册，否则 haecceity、supervenience 这类会反复误报。

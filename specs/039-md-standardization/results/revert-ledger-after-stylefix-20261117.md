# P8 回退面前置台账（2026-11-17）

- 回退面：**55 件**（r3_reviewed 1、s2.5_checked 53、r2_reviewed 1）
- 三轴机检：**绿 37 / 红 18**（绿＝可携机检凭证进入重走，红＝须先修）

## 红灯规则分布

| 规则 | 件次 |
| ---- | ---- |
| `curly-quotes` | 10 |
| `heading-number` | 9 |
| `tail-order` | 5 |
| `quote-spacing` | 2 |
| `bold-spacing` | 1 |

## 阻断件清单（前 60）

| slug | 状态 | 硬错误 |
| ---- | ---- | ---- |
| `actualism-possibilism-ethics` | s2.5_checked | bold-spacing: ** 后缺空格: **它***会 ** 导致… |
| `al-kindi` | s2.5_checked | curly-quotes: 右引号先于左引号: 尽管肯迪的认识论具有上文所述的反经验主义特征，他却为自然科学的各个分支投入了巨大<br>curly-quotes: 右引号先于左引号: 尽管肯迪的认识论具有上文所述的反经验主义特征，他却为自然科学的各个分支投入了巨大 |
| `arabic-islamic-phil-math` | s2.5_checked | curly-quotes: 右引号先于左引号: 柏拉图同时承诺这两条论题。相比之下，毕达哥拉斯派只接受后者。至少若我们信任亚里士 |
| `demonstration-medieval` | s2.5_checked | tail-order: 尾节缺失：参考文献 |
| `early-modern-india` | s2.5_checked | heading-number: 二级标题须点号式 `N. 标题`：1.3 句义清单的底层结构 |
| `egoism` | s2.5_checked | curly-quotes: 右引号先于左引号: 第二个反对伦理利己主义的论证由 H. A. 普里查德提出。他论证说自身利益是错误 |
| `falaquera` | s2.5_checked | quote-spacing: 引号与西文/数字之间缺半角空格: …har ha-he‘der*），或在…<br>quote-spacing: 引号与西文/数字之间缺半角空格: …创造”（*beri‘ah*）的解释，… |
| `ibn-sina` | s2.5_checked | curly-quotes: 引号不成对（‘…’ 差 1）: 亚里士多德的伦理学提供了这座大厦的基础。去认识、并理性地认识的绝对命令——这是阿 |
| `implicature-optimality-games` | s2.5_checked | curly-quotes: 引号不成对（‘…’ 差 1）: 1. $P(i_2 \mid [\![$‘two’$]\!]) = ⅓$ 高于任<br>curly-quotes: 右引号先于左引号: \text{three}{\text{’}} ]\!] \subset [\![<br>curly-quotes: 右引号先于左引号: \text{one}{\text{’}} ]\!], $$ |
| `kaspi-joseph` | s2.5_checked | heading-number: 小节编号跳号：6 → 6 |
| `kilvington` | s2.5_checked | heading-number: 小节编号跳号：6 → 6 |
| `knowledge-how` | s2.5_checked | tail-order: 尾节缺失：参考文献 |
| `korean-philosophy` | s2.5_checked | tail-order: 尾节缺失：参考文献<br>heading-number: 二级标题须点号式 `N. 标题`：3.1 儒学<br>heading-number: 小节编号跳号：2 → 4 |
| `kukai` | s2.5_checked | tail-order: 尾节缺失：参考文献 |
| `nietzsche-aesthetics` | s2.5_checked | heading-number: 二级标题须点号式 `N. 标题`：2.《悲剧的诞生》<br>heading-number: 小节编号跳号：1 → 3 |
| `quine-nf` | s2.5_checked | curly-quotes: 右引号先于左引号: u{\text{’}}) + 1$；若 $<br>curly-quotes: 右引号先于左引号: v{\text{’}}) = \sigma( |
| `representation-medieval` | s2.5_checked | heading-number: 小节编号跳号：4 → 6<br>heading-number: 小节编号跳号：6 → 5 |
| `zhu-xi` | r2_reviewed | tail-order: 尾节缺失：参考文献 |

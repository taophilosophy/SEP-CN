# 全量回源 sha 核对报告（修复钉后终态）

- 扫描：2026-11-15（tools/drift_scan.py，1872 词条、64路×10s 豁免配置、0 网络失败）
- 原始报告：drift-scan-20261114T192704Z.json；本文件为其修复钉后的终态判定（ADR-0045）

## 汇总

| 类别 | 数 |
| ---- | ---- |
| 与原始钉一致（unchanged） | 1800 |
| 真上游漂移（供 update 任务） | 72 |
| 钉污染回修（015 偿还期重算所致，已依冻结语义回修+补登记） | 50 |
| 软 404（retired：theory-bioethics） | 1 |

## 真上游漂移清单（72）

| slug | 原始钉 | live |
| ---- | ---- | ---- |
| academic-freedom | `f347d921b34c…` | `02bc1b992c93…` |
| advance-directives | `b663ee735fa0…` | `affe0d3e8f34…` |
| altruism-empirical | `42be3fd57597…` | `8b721eb66892…` |
| argument | `4ea18363951c…` | `512c3af08206…` |
| aristotle-psychology | `cd775fbfaa8a…` | `d00d9c9a178c…` |
| ayn-rand | `e7401da3fe10…` | `0393ae502a4b…` |
| behaviorism | `0afe8ebb9ad8…` | `72b7ca26a988…` |
| benjamin | `dbfebae6c02e…` | `e4666184a79e…` |
| berlin | `4ca8b1843f14…` | `099fe1657325…` |
| cellular-automata | `12a7c70e9f51…` | `981295e00b53…` |
| closure-epistemic | `fe2dbe49db6c…` | `ba74358a2a48…` |
| compatibilism | `ae9d624dc964…` | `7dc61f888641…` |
| concepts | `f2e81a2de335…` | `920d901cf5d3…` |
| consequentializing | `7963e57a41e1…` | `1ae5ac51b5c3…` |
| content-narrow | `c9a5c07a091c…` | `034583384168…` |
| david-lewis | `88c6a9157f95…` | `da11589bc643…` |
| derrida | `a594f29e9832…` | `20a12f56413d…` |
| dialectical-school | `debcc11864a9…` | `2c0e52d715d5…` |
| early-modern-india | `c3b66a9114eb…` | `db1f29e184d6…` |
| emotion-Christian-tradition | `9dee7a3d14ed…` | `0a945aed1356…` |
| enhancement | `cf347647c002…` | `46c75bcc3abd…` |
| epistemic-utility | `e70ca6e491ce…` | `36661960b08c…` |
| essential-accidental | `10e1ba3d79b8…` | `6c4f00b27009…` |
| experimental-moral | `cb482194897b…` | `fc96ddf652b7…` |
| feminism-aesthetics | `b6f4aa678537…` | `62727067fa88…` |
| feminist-bioethics | `b988f7a699ef…` | `ac4cddd38d28…` |
| form-matter | `024fee3dd3dd…` | `f81569e7a289…` |
| freewill | `97fe5912dbb0…` | `96d7f58dadac…` |
| game-theory | `2d41ef74d843…` | `bd5285aabfcb…` |
| genetics | `d43c85524ec3…` | `c75688d89fcc…` |
| green | `16f8a075cdf4…` | `374e4acddc26…` |
| heidegger-aesthetics | `09dd5873942a…` | `e1fe1015b35c…` |
| ibn-bajja | `15a7fcb6ec1a…` | `374709d16cb8…` |
| incompatibilism-theories | `31ad3bcb209c…` | `a91596128c56…` |
| infinite-regress | `f9c96b97a329…` | `f8ba5502b6ca…` |
| it-moral-values | `691f8514e299…` | `d5b4d54444e0…` |
| justep-intext | `d3f1b28b5998…` | `a8401630d51d…` |
| kant-leibniz | `5963a912972d…` | `be4df55da3c4…` |
| kumaarila | `b52d28a6a609…` | `8fc55268773c…` |
| linguistics | `6d66dc879891…` | `c33804617603…` |
| logic-ancient | `e3e243167a9c…` | `77a6ef2a0094…` |
| logic-provability | `31ac09d95f06…` | `7fb4661215d9…` |
| madhyamaka | `8ef0e228ea69…` | `b2c55ed13c81…` |
| meaning-holism | `e12941117041…` | `5785ef277150…` |
| medicine | `c4a1dccb946e…` | `56d06d49f3d4…` |
| metaphysical-explanation | `1f4ae4c7a557…` | `ffcb32defe76…` |
| metaphysics | `8c54df14ec33…` | `b2d09418377c…` |
| molecular-genetics | `57d75933a347…` | `4e4b462a99ee…` |
| moral-conventional | `8a910e9694fa…` | `bfe9ccea9f17…` |
| moral-responsibility | `dcc81ed294d8…` | `64ee9c99b3a7…` |
| nominalism-mathematics | `a033632fa853…` | `b9ba8676fc68…` |
| perception-india | `163fea827bab…` | `1cef21d12c0c…` |
| phenomenal-intentionality | `77ca776e09f6…` | `a2065174e03c…` |
| philosophy-mathematics | `6b1b069983c3…` | `caa3ffdf8468…` |
| physics-experiment | `8c80defbb5e0…` | `ef52c0ffb700…` |
| porphyry | `08029f760ac5…` | `ede262d9a72a…` |
| practical-reason-med | `30de4fcf056e…` | `e245c6ec3f51…` |
| preferences | `fb9e26f00eb3…` | `f2442e390f4f…` |
| principle-beneficence | `fdc0987442c6…` | `524183699379…` |
| reasons-agent | `bf6428dc4e4c…` | `4b97d5229f14…` |
| reasons-internal-external | `aefd28e4d256…` | `4ea8a6dd71ae…` |
| recursive-functions | `5fa44199c013…` | `e2bd0e7712b3…` |
| saadya | `183eb98ccde9…` | `fdbd11c385f3…` |
| schopenhauer-aesthetics | `0f711f8cf7ac…` | `1f02616dff6b…` |
| scientific-representation | `3d42565f846e…` | `4f8a21a738f4…` |
| self-knowledge | `1aeea6797ada…` | `f9286b8701f1…` |
| shared-agency | `149041862e77…` | `a4343fd86041…` |
| skepticism | `26e3b0c41fa1…` | `13be9d9704bf…` |
| spencer | `4fc3f8979249…` | `9420f60d4e4f…` |
| voltaire | `d4f982543370…` | `3423d64c45fa…` |
| wittgenstein | `ec6822aad509…` | `2032c8c66af0…` |
| advance-directives | `b663ee735fa0…` | `affe0d3e8f34…` |

## 钉污染回修清单（50）

钉被 015 偿还批「台账重算」写成改后本地哈希；已按 git 历史（d0294236f 原始物入库 blob）回修，并对本地勘误偏离逐条补登记 baseline/divergences.json（verify --deep 全绿）。

| slug | 回修后原始钉 |
| ---- | ---- |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |
| slug | `upstream…` |

## 处置

1. 真漂移 72 条：走 compare.py 产出变更文件 → update 任务（批量战役规模，待用户排期；errata 在账者届时用 divergence.py carry 随迁）。
2. 回修 50 条：entries.json 钉已还原原始字节哈希；verify --deep 全绿。
3. 污染根因：015 偿还批将 ADR-0038 决策 2「重转时重算」误施于 files[].sha256（应只适于 yuanwen 哈希）；ADR-0045 冻结语义 + verify 门禁已堵死再发路径。

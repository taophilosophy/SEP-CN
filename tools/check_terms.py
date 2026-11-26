# -*- coding: utf-8 -*-
"""术语一致性检查器（specs/002 FR-001..005；ADR-0012/specs/008 扩展双表；ADR-0036 词汇表并网）。

用法:
  python tools/check_terms.py                       # 两登记册自洽（门禁）
  python tools/check_terms.py --docs a/某词条.md …   # 定点核销：登记册"首现"驱动的正文核对
  python tools/check_terms.py --ledger <路径> --docs a/某词条.md …
                                                    # 定点核销 + 判读台账骨架（ADR-0048 决策 6，specs/031 FR-1）
  python tools/check_terms.py --check-ledger <路径> # 台账闭合校验（D 类/三出口/凭证，specs/031 FR-2）
  python tools/check_terms.py --registry <路径>     # 测试注入（单表模式）
  python tools/check_terms.py --registry2 <路径>    # 注入第二登记册（人名表）

两表（ADR-0036 2026-11-13：发布词汇表 qian-yan/ci-hui-biao.md 已并网删除，三表收敛为双表）:
  - 术语登记册 shu-yu-biao.md（键|原文|译法|首现|依据|裁定日期，六列；
    旧五列「键|译法|首现|依据|裁定日期」按旧口径兼容解析）
  - 人名登记册 ren-ming-biao.md（同六列，ADR-0012 自术语表拆出）

规则:
  - 键规范化：剥 * 斜体标记、去首尾空格、比对用 casefold，展示保留原样。
  - 译法集合：取"（"前主形，并按 / 与 ／ 拆分为变体（--docs 定点核销按变体命中判定）。
  - 登记册自洽：废弃行须有同键非废弃行；裁定日期缺失、依据列缺失 = 告警
    （数据欠账，登记会话补齐）；同键同译法重复 = 硬错误。
  - 非英语术语缺原文 = 提醒（非硬错误；ADR-0087 2026-11-26 定性，原 2026-11-06 告警）：
    键含非 ASCII 拉丁变音符／非拉丁文字，或命中内置小语种词表者，「原文」列为「—」
    或空（旧五列无该列亦视为缺）即记一条；查无显式配对留「—」为合规终态，清单落
    specs/008 results/orig-missing.txt。
  - 审定引用配对 = 告警（非硬错误，ADR-0088 2026-11-26）：依据声明审定命中、但按
    配对判据（tools/term_pairing.py）无 pairing 且行内无说明的行；索引缺失时跳过。
    判据口径见 ADR-0090（豁免词只认精确短语、待判文本只取依据列、多形译法拆形）。
  - 引证库名如实 = 告警（非硬错误，ADR-0088 第 2 条／ADR-0090 2026-11-26）：行内
    「审定…作“X”」所声称的库别与索引内 X 的实际库别不符，或同段既称审定又称
    对照库／其他库；带条文号的纸质引证跳过。清单落 specs/058 results/citation-lib-warnings.txt。
  - 人名首现悬空 = 告警（2026-11-26）：人名表「首现」列写成 slug 形状但 en/ 下无该词条
    目录（ADR-0009 目录命名）；「语料回收（…）」「首现（…）」「—」等非 slug 标注不判。
    清单落 specs/013 results/person-dangling-first.txt。
  - 术语首现悬空 = 告警（2026-11-26，同口径）：术语登记册「首现」列的裸 slug、
    `<letter>/<slug>`、`<slug>.supplement`（落 en/<base>/supplement.html）与括注里的
    ASCII 词条名逐条校验；散文标注不判。清单落 specs/058 results/term-dangling-first.txt。
退出码: 0 无硬错误；1 有冲突或自洽违例（--docs 模式仅告警，恒 0；--check-ledger 违例 1）；
        2 参数错误（如 --ledger 未配 --docs）。
"""
import io
import json
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)  # 脚本直跑时保证 from tools import 可用
# 解析/折叠原语唯一实现（specs/033）：norm_key 仍是 A 引号折叠键口径
# （= register_lib.norm_key_quote），比对语义不变；B/C 口径见 register_lib。
from tools.register_lib import (HEADER_WORDS, is_data_row,  # noqa: E402,F401
                                norm_key_quote as norm_key,
                                parse_registry, parse_registry2_full,  # noqa: E401,F401
                                parse_registry_full,  # noqa: E401,F401
                                person_path, split_row, term_path)  # noqa: E401,F401
from tools import term_pairing  # noqa: E402  ADR-0088 配对判据共享实现
REGISTRY = term_path()
REGISTRY2 = person_path()
ORIG_REPORT = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                           'orig-missing.txt')
PERSON_REPORT = os.path.join(ROOT, 'specs', '013-person-attribution', 'results',
                             'person-missing.txt')
PERSON_FIRST_REPORT = os.path.join(ROOT, 'specs', '013-person-attribution', 'results',
                                   'person-dangling-first.txt')
PAIR_INDEX = os.path.join(ROOT, term_pairing.INDEX_PATH)
STD_PAIR_INDEX = os.path.join(ROOT, term_pairing.STD_INDEX_PATH)
STD_PAIR_REPORT = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results',
                               'std-pairing-warnings.txt')
PAIR_REPORT = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results',
                           'term-pairing-warnings.txt')
LIB_REPORT = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results',
                          'citation-lib-warnings.txt')
DEPRECATED_MARK = '已废弃'
# 判读台账（ADR-0048 决策 6，specs/031）：机器只写事实，D 类/出口/凭证/复核人留空待人填
LEDGER_SCHEMA = 'sep-cn-term-ledger/1'
D_CLASSES = ('D1', 'D2', 'D3', 'D4', 'D5', 'n/a')
LEDGER_EXITS = ('fix', 'register', 'exempt')
# 译法列尾段疑似词条 slug（小写拉丁＋连字符，前面带分号）：中文译法不会以此收尾
SLUG_TAIL_RE = re.compile(r'；\s*[a-z][a-z0-9]*(?:-[a-z0-9]+)*\s*$')

# 原文列视为「缺」的写法（迁移占位符；英文术语按体例同样填「—」，但不算缺）
ORIG_BLANK = {'', '—', '–', '--', '-', '－', '——', 'n/a', 'na', '无'}

# 非英语术语词表（008 战役·原文列迁移 2026-11-06 新增告警用）：
# 只收两登记册实际出现的拉丁惯用语／德／法／阿拉伯转写／梵巴藏转写／
# 希腊转写／日／朝／汉语拼音条目；比对口径＝casefold 后的整键、去括注主形、
# 括注内容与「/」拆分变体（键里括注常直接给出转写原文）。条目以 | 分隔，
# 允许含空格的多词短语（mysterium tremendum et fascinans 等）。
FOREIGN_WORDS = frozenset(
    w.strip() for line in """
ampliatio|consequentia|incipit|desinit|ens inquantum ens|ex nihilo
ex contradictione quodlibet|modus ponens|modus tollens|modus significandi
modi significandi|sophisma|sophismata|nota illationis|praedicamentum signi
per se|per se predication|prima facie|bona fide|ceteris paribus|tabula rasa
vis aestimativa|vis copulativa|vis viva|secundum imaginationem
potentia dei absoluta|potentia dei ordinata|instantiae naturae|beneplacitum
scientia necessaria|ad utrumlibet|velle|nolle|non-velle|venerabilis inceptor
scientia|cognitio|cogito|sensus communis|sensus divinitatis|esse habituale
obligatio|obligationes|casus|significatio|nominatio|singularia
syncategorematica|synsemantica|entia rationis|insolubilia|superadditum
libertas philosophandi|ius ubique docendi|magna charta universitatum
novum organum|de revolutionibus|de sophisticis elenchis|collegia pietatis
stare decisis|ratio decidendi|paradeigma|homoiotes|reductio|definiens
definiendum|a priori|a posteriori|de dicto|de re|a fortiori|quodlibet
quaestio|opus postumum|complexe significabile|delectatio|caritas|monarchia
mysterium tremendum et fascinans|quidditas|haecceitas|via moderna|via antiqua
ars inveniendi|ars iudicandi|dictum|proslogion|george-kreis
logos|nous|telos|polis|pathos|doxa|mimesis|pneuma|hegemonikon|ataraxia
pleonexia|sophrosune|dikaiosune|kalokagathos|euthymia|antitupia|sunkrisis
poroi|kenon|aphanes|phusis|nomos|isonomia|metabasis|physiologos|physiologoi
ou mallon|aporeia|epagoge|eudaimonia|tekmairesthai
begriffsschrift|bedeutung|bildung|dasein|sittlichkeit|vorstellung|erlebnis
erfahrung|darstellung|ereignis|sache selbst|werden|nacherleben
gewissenstrieb|bestimmung|lehrfreiheit|lernfreiheit|elementarphilosophie
satz des bewusstseins|tathandlung|wissenschaftslehre|denken als denken
sprachloses denken|synonymik|gehalt|aufhebung|weltanschauung|verstehen
lebenswelt|umwelt|mitsein|vorhandenheit|zuhandenheit
petites perceptions|je ne sais quoi|fait social|le monde|raison d'etre
falsafa|fitra|sunna|fiqh|hadith|kalam|sharia|ijma|qiyas|ijtihad|taqlid
tawhid|tasawwuf|sufi|hikma|mahdi|umma|madhhab|falasifa|mutakallimun
tahafut|ishraq|mashsha'i
dharma|karma|mantra|yoga|tantra|sutra|sastra|shastra|abhidharma|abhidhamma
vinaya|vipassana|samatha|nirvana|moksha|atman|anatman|brahman|prajna
karuna|metta|dukkha|anicca|anatta|jhana|stupa|arhat|bodhisattva|skandha
dhatu|ayatana|pratityasamutpada|madhyamaka|apoha|icchantika|chakravarti
gotra|hetu|phala|nirodha|tanha|samsara|kensho|satori|koan
tshad ma|snang yul|gzung yul|zhen yul|blo|blo rigs|nges pa|bsdus grwa
bsdus pa|gzhan sel|rnam pa|sgra spyi|don spyi|rjod byed|brjod bya|sgra don
bcad shes|yid dpyod|log shes|the tshom|ma rtogs|dngos rtogs|shugs rtogs
rigs gter|snang la ma nges pa|rtog pa|tshad ma rigs gter|tshad ma'i bsdus pa
ngo bo gcig la ldog pa tha dad|'jug yul|sefer ha-zohar
wabi|sabi|wabi-sabi|iki|kire|kireji|karesansui|seppuku|engi|kata|tokonoma
haboku|hatsuboku|kara-e|yamato-e|sansui|meibutsu|basara|nijiriguchi
kakemono|bitai|ikiji|akirame|kire-tsuzuki|sabireru|sabishii|shibumi|amami
jimi|gehin|katanakake|kokugaku|kokugakusha|shinkoku|magokoro|karagokoro
mikunigokoro|kannagara|kishin|saisei itchi|kokutai|nihonjinron|hongaku
mono no aware|wabicha|raku|shoin
qi|tian|dao|yin|yang|wuwei|wu wei|daodejing|lunyu|lun yu|mengzi|mozi
zhuangzi|laozi|lao tzu|xunzi|han feizi|yijing|i ching|tao te ching
huainanzi|shiji|liezi|guanzi|chunqiu|analects
hwajaeng|hwalgu|sagu|minjung|yixin|ilsim|tong pulgyo
gulag|cheka|partinost|samizdat
""".strip().splitlines() for w in line.split('|') if w.strip())

# 阿拉伯/波斯人名转写标记（Ibn Sīnā、al-Fārābī 等；ASCII 拼写也须给原文）
_ARABIC_NAME_RE = re.compile(r'\b(?:ibn|bint|abu)\b|\bal-[a-z]')
_PAREN_RE = re.compile(r'[（(]([^（）()]*)[）)]')
_VARIANT_SPLIT = re.compile(r'[/／]')


def translations(cell):
    """译法集合：主形按 / ／ ； 、 ; ， 拆分变体；并吸收注记里的
    亦作"X"/译作"X"（半/全角引号，含"X""Y"连排）变体与书名号《X》主形
    （008 战役比对口径，2026-10-29；译作 与连排引号 2026-10-30 落地复核补）。"""
    body = re.sub(r'^（[^）]*）', '', cell)   # 「（思想的）副词论」型：先剥前缀括注
    head = body.split('（')[0].strip()
    variants = {v.strip() for v in re.split(r'[/／；、;，]', head) if v.strip()}
    for m in re.finditer(r'(?:亦作|译作)[“"]([^”"]{1,40})[”"]', cell):
        for v in re.split(r'[/／；、;，]', m.group(1)):
            if v.strip():
                variants.add(v.strip())
        rest = cell[m.end():]                 # 连排引号："X""Y"
        while True:
            m2 = re.match(r'[“"]([^”"]{1,40})[”"]', rest.strip())
            if not m2:
                break
            for v in re.split(r'[/／；、;，]', m2.group(1)):
                if v.strip():
                    variants.add(v.strip())
            rest = rest.strip()[m2.end():]
    for m in re.finditer(r'《([^《》]{1,60})》', cell):
        variants.add(m.group(1).strip())
    return {v for v in variants if v}


FIRST_PATH_RE = re.compile(r'^([a-z])/([A-Za-z0-9][A-Za-z0-9_.-]*)$')
# 裸 slug 必须含小写字母：全大写者是「SUMMARY」一类标注词，不是词条名
FIRST_SLUG_RE = re.compile(r'^(?=.*[a-z])[A-Za-z0-9][A-Za-z0-9_.-]*$')


def person_dangling_first(rows2):
    """人名表「首现」列的词条引用是否落地；同时报非规范的路径形（告警）。

    首现列允许三类值：裸 slug（en/<slug>/ 存在）、`<letter>/<slug>` 路径形（ADR-0009
    的目录形，可解但非规范，应归一为裸 slug）、散文标注（语料回收（…）、SUMMARY 定名
    （…）、—）；以「；」分段逐段判。返回 (悬空, 非规范形)，元素为
    (term, 列值, 行号, 归一后的 slug)。判据与 ADR-0009 的目录命名同源：只认 ASCII 词条名。"""
    en_dir = os.path.join(ROOT, 'en')
    bad, informal = [], []
    for (term, _orig, _trans, _nation, _years, fs, _basis, _date, lineno) in rows2:
        for part in re.split(r'[；;]', fs or ''):
            p = part.strip()
            if not p:
                continue
            m = FIRST_PATH_RE.match(p)
            if m:
                slug = m.group(2)
                if os.path.isdir(os.path.join(en_dir, slug)):
                    informal.append((term, p, lineno, slug))
                else:
                    bad.append((term, p, lineno, slug))
                continue
            if FIRST_SLUG_RE.match(p):
                if not os.path.isdir(os.path.join(en_dir, p)):
                    bad.append((term, p, lineno, ''))
    return bad, informal


TERM_FIRST_REPORT = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results',
                                 'term-dangling-first.txt')


def _first_targets(fs):
    """从首现列取可校验的词条引用：裸 slug、`<letter>/<slug>`、`<slug>.supplement`
    以及括注里的 ASCII 词条名（首现（wisdom）一类）。散文标注不产引用。"""
    text = fs or ''
    out = []
    for m in re.finditer(r'[（(]([A-Za-z0-9][A-Za-z0-9_.-]*)[）)]', text):
        if re.search(r'[a-z]', m.group(1)):
            out.append(m.group(1))
    s = text.strip()
    if FIRST_SLUG_RE.match(s):
        out.append(s)
    else:
        m = FIRST_PATH_RE.match(s)
        if m:
            out.append(m.group(2))
    return out


def _first_exists(ref):
    """`X.supplement` 落在 en/X/supplement.html；其余按 en/<slug>/ 目录判。"""
    m = re.match(r'^(.+)\.supplement$', ref)
    if m:
        return os.path.exists(os.path.join(ROOT, 'en', m.group(1), 'supplement.html'))
    return os.path.isdir(os.path.join(ROOT, 'en', ref))


def term_dangling_first(rows):
    """术语登记册「首现」列的词条引用是否落地（告警，不判散文标注）。

    rows 为 load_one 口径 (term, trans, fs, basis, date, lineno)。补编式
    `geometry-19th.supplement` 是合法写法，落到 en/<base>/supplement.html。"""
    bad = []
    for (term, _trans, fs, _basis, _date, lineno) in rows:
        for ref in _first_targets(fs):
            if not _first_exists(ref):
                bad.append((term, ref, lineno))
    return bad


PERSON_TERMINAL_RE = re.compile(r'终态|NOSOURCE')
PERSON_TERMINAL_SOFT_RE = re.compile(r'不适用|无考|不传|未见|不详|留空|留白|无来源|无权威')
PERSON_PENDING_RE = re.compile(r'待考|待补|待查|待核|待定')

# 013 判定台账（2026-11-26）：终态不写回登记册（013 两档方案明令 B 档不追加
# 记录），由本工具读台账作机检豁免源；台账缺失即退化，不影响硬错误判定。
PERSON_TERMINAL_LEDGERS = (
    ('specs/013-person-attribution/results/per-line-adjudication-2026-11-20.jsonl',
     'per-line'),
    ('specs/013-person-attribution/results/gnd-triage-2026-11-26.tsv', 'triage'),
    ('specs/013-person-attribution/results/gnd-review-decisions-2026-11-26.tsv',
     'decisions'),
)
_PERSON_TERMINAL_CACHE = None


def load_person_terminal_keys():
    """返回 {键: 来源} —— 013 已判终态的缺项人名。

    来源：
      * per-line-adjudication v=NOSOURCE：逐人查无、留空（含 B 档历史判定）
      * gnd-triage verdict=none：GND 无任何候选
      * gnd-review-decisions 判定“驳回/同名驳回”，或判定“未判”且候选生卒为空
        （B 档“查无确年”）
    """
    global _PERSON_TERMINAL_CACHE
    if _PERSON_TERMINAL_CACHE is not None:
        return _PERSON_TERMINAL_CACHE
    out = {}

    def base(rel):
        return os.path.join(ROOT, rel.replace('/', os.sep))

    for rel, kind in PERSON_TERMINAL_LEDGERS:
        p = base(rel)
        if not os.path.exists(p):
            continue
        if kind == 'per-line':
            with open(p, encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        row = json.loads(line)
                    except ValueError:
                        continue
                    if row.get('v') == 'NOSOURCE':
                        out.setdefault((row.get('key') or '').strip().casefold(),
                                       'per-line')
        elif kind == 'triage':
            with open(p, encoding='utf-8') as f:
                next(f, None)
                for line in f:
                    c = line.rstrip('\n').split('\t')
                    if len(c) >= 2 and c[1].strip() == 'none':
                        out.setdefault(c[0].strip().casefold(), 'triage')
        elif kind == 'decisions':
            with open(p, encoding='utf-8') as f:
                next(f, None)
                for line in f:
                    c = line.rstrip('\n').split('\t')
                    if len(c) < 8:
                        continue
                    verdict = c[6].strip()
                    if verdict in ('驳回', '同名驳回'):
                        out.setdefault(c[0].strip().casefold(), 'decisions')
                    elif verdict == '未判' and not re.search(r'\d{3,4}', c[2] or ''):
                        out.setdefault(c[0].strip().casefold(), 'decisions')
    _PERSON_TERMINAL_CACHE = out
    return out


def _person_lack(rows2):
    """逐行产出 (term, lineno, 缺项, terminal, source)。

    终态判据（2026-11-26）：依据列明确写「终态」或「NOSOURCE」即豁免；写
    「不适用/无考/不传/未见/不详/留空/留白/无来源/无权威」且不带「待考/待补/
    待查/待核/待定」的也豁免（「留空并登记」是结论，「留白待考」是待办）。另读
    013 台账的 NOSOURCE／GND none／驳回 判定作豁免源（load_person_terminal_keys）。
    **显式待办优先**：依据列含待考类词时，台账不得覆盖（2026-11-26 审查修正）。
    豁免只影响告警与清单，不改登记册。
    """
    terminal_keys = load_person_terminal_keys()
    for (term, _orig, _trans, nation, years,
         _fs, _basis, _date, lineno) in rows2:
        lack = []
        if nation is None or nation.strip() in ORIG_BLANK:
            lack.append('籍属')
        if years is None or years.strip() in ORIG_BLANK:
            lack.append('生卒/鼎盛年')
        if not lack:
            continue
        basis = _basis or ''
        pending = bool(PERSON_PENDING_RE.search(basis))
        source = None
        if PERSON_TERMINAL_RE.search(basis):
            source = 'basis'
        elif PERSON_TERMINAL_SOFT_RE.search(basis) and not pending:
            source = 'basis'
        if source is None and not pending:
            source = terminal_keys.get((term or '').strip().casefold())
        if source is not None:
            yield term, lineno, '、'.join(lack), True, source
            continue
        yield term, lineno, '、'.join(lack), False, None


def person_missing(rows2):
    """人名缺「籍属」「生卒/鼎盛年」且未判终态：返回 [(term, lineno, 缺项)]。

    rows2 为 parse_registry2_full 口径；nation/years 为 None（旧六列）或空/「—」
    都记为缺。只对人物登记册调用。已判终态行不计入（见 _person_lack）。
    """
    return [(t, ln, lack) for t, ln, lack, terminal, _src in _person_lack(rows2)
            if not terminal]


def person_terminal_stats(rows2):
    """已判终态的缺项行：返回 (总数, 按来源计数 dict)。"""
    cnt = {}
    total = 0
    for _t, _ln, _lack, terminal, source in _person_lack(rows2):
        if terminal:
            total += 1
            cnt[source] = cnt.get(source, 0) + 1
    return total, cnt


def write_person_terminal_index(rows2, path):
    """生成终态索引（供审计，不写登记册）：键\t行号\t缺项\t来源。"""
    lines = []
    for term, lineno, lack, terminal, source in _person_lack(rows2):
        if terminal:
            lines.append('%s\t%d\t%s\t%s' % (term, lineno, lack, source))
    _atomic_write(path, '\n'.join(lines) + '\n' if lines else '')
    return len(lines)




def _atomic_write(path, text):
    """原子写报告，带并发退避（specs/052：8 路并行回补时 os.replace 撞车）。

    原实现用固定 `.tmp` 名且无重试：并发调用时一方已把 tmp 改名，另一方的
    os.replace 抛 WinError 2/5/32，整个进程以 1 退出——判官崩溃被上层读成
    "该件术语门禁未通过"，是**假阳性**。tmp 名带 pid 消除同党争抢，重试消解
    目标句柄被瞬时占用。
    """
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    tmp = "%s.%d.tmp" % (path, os.getpid())
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    last = None
    for _ in range(60):
        try:
            os.replace(tmp, path)
            return
        except OSError as exc:      # WinError 5/32：对方仍持有目标句柄
            last = exc
            time.sleep(0.05)
    try:
        os.unlink(tmp)
    except OSError:
        pass
    raise last


def write_person_missing(entries, path, terminal=0):
    """person-missing.txt：每行「人名\t行号\t缺项」，末行汇总（原子写）。

    terminal 为已判终态、未计入 entries 的行数（2026-11-26 起单列，便于读进度）。
    """
    lines = ['%s\t%d\t%s' % e for e in entries]
    lines.append('汇总\t%d\t人名缺籍属/生卒（已判终态 %d 条未计入）'
                 % (len(entries), terminal))
    _atomic_write(path, '\n'.join(lines) + '\n')



def has_foreign_char(text):
    """键里是否有非 ASCII 字母/变音符（拉丁变音符、希腊/阿拉伯/梵/汉/谚文假名）。

    只认 Unicode 字母类与组合附加符（L*/M*）：全角括号、弯引号、破折号等
    西文标点不算（"justified true belief（JTB）" 不应判为非英语）。
    """
    import unicodedata
    for ch in text:
        if ord(ch) > 127 and unicodedata.category(ch)[0] in ('L', 'M'):
            return True
    return False


def _key_variants(term):
    """键 → 比对变体：整键、去括注主形、每条括注内容，再按「/」拆分。

    弯引号统一为直引号，并另出「去撇号」形（T’ong Pulgyo → tong pulgyo，
    朝鲜/藏文转写常用 ’ 表音）。
    """
    out = set()

    def add(s):
        s = re.sub(r'\s+', ' ', s.strip()).replace('’', "'")
        if not s:
            return
        out.add(s.casefold())
        bare = re.sub(r"['\u02bc`]", '', s)
        if bare != s:
            out.add(bare.casefold())

    add(term)
    add(_PAREN_RE.sub(' ', term))
    for m in _PAREN_RE.finditer(term):
        inner = m.group(1)
        add(inner)
        for v in _VARIANT_SPLIT.split(inner):
            add(v)
    for base in list(out):
        for v in _VARIANT_SPLIT.split(base):
            add(v)
    return out


def is_non_english(term):
    """非英语术语判定：非 ASCII 字母/变音符、阿拉伯人名转写、小语种词表。"""
    if has_foreign_char(term):
        return True
    if _ARABIC_NAME_RE.search(term.casefold()):
        return True
    return any(v in FOREIGN_WORDS for v in _key_variants(term))


# 英文术语键附「编者括注」豁免（012 阶段1，2026-11-07）：键中 CJK 仅为语境/概念域
# 编者注而非源语言原文，基准词是英文词，原文列恒「—」：
#   - competence（医疗与法律语境）：organ-donation 法学与医学语境消歧注
#   - yielding（虚空）：democritus「虚空让与」概念域注（虚空本体另有键 kenon）
ORIG_EDITORIAL_PAREN = frozenset({
    'competence（医疗与法律语境）', 'yielding（虚空）',
    'anarchy（国际关系）', 'token（令牌环语境）',
    # 2026-11-10 补遗：键含编者括注或非英语专名，但基准词为英文，原文列恒「—」
    'ontology (Leśniewski)', 'proper function（普兰丁格认识论）',
    'chimera（生物医学语境）', 'Gödel encoding',
    'Ł-modal system', 'modal μ-calculus',
    # 2026-11-20 全量复核补遗：
    #   Great Learning（王阳明《大学问》）——键为英文题名，中文括注系同形异义分行标记（ADR-0048）
    #   Löwenheim–Skolem–Tarski theorem——英文定理名，含 ö 致 is_non_english 误命中
    'Great Learning（王阳明《大学问》）', 'Löwenheim–Skolem–Tarski theorem',
    # 2026-11-25 补遗：英文题名＋作者括注（肯迪著作与“第一哲学”通名分行）
    'On First Philosophy (al-Kindi)',
})


def _paren_norm(s):
    """全角/半角括注归一：白名单按全角登记，登记册里半角写法也须命中。

    2026-11-25 修：anarchy（国际关系）等 7 条早已在白名单，却因登记册写作半角
    “anarchy(国际关系)”而继续告警——比对时未归一括号形态。
    """
    return s.replace('\uff08', '(').replace('\uff09', ')')


ORIG_EDITORIAL_PAREN_N = frozenset(_paren_norm(x) for x in ORIG_EDITORIAL_PAREN)


def orig_missing(rows):
    """「非英语术语缺原文」：rows 为 parse_registry_full 口径，返回 [(键, 行号)]。

    原文列为「—」或空即记；旧五/四列格式无原文列（orig=None），迁移未完成的
    行同样计入（本告警即迁移清单）。
    """
    out = []
    for term, orig, _trans, _fs, _basis, _date, lineno in rows:
        if orig is not None and orig.strip() not in ORIG_BLANK:
            continue
        if _paren_norm(term) in ORIG_EDITORIAL_PAREN_N:
            continue
        if is_non_english(term):
            out.append((term, lineno))
    return out


def write_orig_missing(entries, path):
    """orig-missing.txt：每行「表\t键\t行号」，末尾一行汇总计数（原子写）。"""
    lines = ['%s\t%s\t%d' % e for e in entries]
    counts = {}
    for label, _term, _lineno in entries:
        counts[label] = counts.get(label, 0) + 1
    detail = ' + '.join('%s %d' % (k, v) for k, v in sorted(counts.items()))
    lines.append('汇总\t%d\t非英语术语缺原文%s'
                 % (len(entries), '（%s）' % detail if detail else ''))
    _atomic_write(path, '\n'.join(lines) + '\n')


def audit_basis_pairs(rows, index):
    """审定引用配对检查（ADR-0088）：依据声明审定命中（无否定、无说明措辞）、
    且按配对判据非 pair 的行 → 告警清单 [(键, 译法, 档位, 行号)]。
    说明措辞默认只看依据列；译法列自身写有“审定…”时才并入（见 claim_text）。"""
    bad = []
    for term, trans, _fs, basis, _date, lineno in rows:
        # 译法列的括注里引出审定形（“审定收「X」”等）也算行内交代，整行放行
        if term_pairing.explicit_citation(trans):
            continue
        if not term_pairing.needs_pairing(term_pairing.claim_text(trans, basis)):
            continue
        v, _ev = term_pairing.classify_row(term, trans, basis, index)
        if v != 'pair':
            bad.append((term, trans, v, lineno))
    return bad


def audit_std_pairs(rows, index):
    """GB 标准库引用配对检查（ADR-0088 同判据）：主张标准库命中、实际无配对的行。"""
    bad = []
    for term, trans, _fs, basis, _date, lineno in rows:
        if not term_pairing.needs_std_pairing(term_pairing.claim_text(trans, basis)):
            continue
        v, _ev = term_pairing.classify_std_row(term, trans, basis, index)
        if v != 'pair':
            bad.append((term, trans, v, lineno))
    return bad


def write_pair_warnings(entries, path):
    """term-pairing-warnings.txt：每行「键\t译法\t档位\t行号」，末尾汇总（原子写）。"""
    lines = ['%s\t%s\t%s\t%d' % e for e in entries]
    lines.append('汇总\t%d\t审定引用无配对（ADR-0088）' % len(entries))
    _atomic_write(path, '\n'.join(lines) + '\n')


def write_lib_warnings(entries, path):
    """citation-lib-warnings.txt：每行「说明\t行号」，末尾汇总（原子写）。"""
    lines = ['%s\t%d' % e for e in entries]
    lines.append('汇总\t%d\t引证库名失实（ADR-0088 第 2 条）' % len(entries))
    _atomic_write(path, '\n'.join(lines) + '\n')


def check_registry_self(rows):
    """自洽性：废弃链、重复 = 硬错误；缺裁定日期/缺依据 = 告警（数据欠账）。"""
    errors, warns = [], []
    by_key = defaultdict(list)
    for term, trans, _fs, _basis, date, lineno in rows:
        by_key[norm_key(term)].append((term, trans, date, lineno))
    for key, items in by_key.items():
        live = [it for it in items if DEPRECATED_MARK not in it[1]]
        deprecated = [it for it in items if DEPRECATED_MARK in it[1]]
        if deprecated and not live:
            errors.append('废弃链断裂：%s 仅剩废弃行（第 %s 行），无有效新行'
                          % (deprecated[0][0], '/'.join(str(it[3]) for it in deprecated)))
        seen = {}
        for term, trans, date, lineno in items:
            if not date or set(date) <= set(':- '):
                warns.append('缺裁定日期（告警）：%s（第 %d 行）' % (term, lineno))
            # 译法列混入词条 slug（2026-11-10 补遗）：合并脚本曾把来源 slug 写进第 3 列，
            # 使 slug 被当作译法变体参与比对（词汇表滞后伪欠账 3 项即由此而来）。
            if SLUG_TAIL_RE.search(trans):
                errors.append('译法列混入词条 slug：%s（第 %d 行）「%s」——slug 属词条列'
                              % (term, lineno, trans.strip()))
            sig = (norm_key(term), trans.strip())
            if sig in seen:
                errors.append('重复行：%s|%s 第 %d 行与第 %d 行重复'
                              % (term, trans, seen[sig], lineno))
            else:
                seen[sig] = lineno
        # 同键异译分立（告警，2026-11-04）：多行不同主形应合并为「主形（亦作…）」体例
        if len(live) > 1:
            mains = []
            for it in live:
                main = re.split(r'[；;（(]', it[1])[0].strip()
                if main:
                    mains.append(main)
            if len(set(mains)) > 1:
                warns.append('同键异译分立（告警）：%s 有 %d 行不同主形（%s），建议合并为亦作体例'
                             % (live[0][0], len(live), '、'.join(dict.fromkeys(mains))))
    return errors, warns


def _ledger_row(doc, term, trans, variants, head, status):
    """台账行骨架：事实字段填好，判读字段留空（specs/031 FR-1）。"""
    return {
        'doc': doc,
        'term': term,
        'translation': trans,
        'variants': sorted(v for v in variants if v),
        'head': head,
        'status': status,
        'd_class': '',
        'exit': '',
        'evidence': '',
        'source': '',
        'reviewer': '',
    }


def write_ledger(path, rows, docs):
    """写判读台账骨架（specs/031 FR-1）：只落事实与待填字段，不预填 D 类。"""
    payload = {
        'schema': LEDGER_SCHEMA,
        'at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'docs': list(docs),
        'rows': rows,
    }
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write('\n')


def check_ledger(path):
    """台账闭合校验（specs/031 FR-2）：D 类/三出口/处置依据/查证凭证/复核人齐全。

    只校验台账自身，不读登记册、不跑正文核销；闭合返回 0，违例返回 1。
    """
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        print('台账不可读: %s（%s）' % (path, e))
        return 1
    errs = []
    if not isinstance(data, dict) or data.get('schema') != LEDGER_SCHEMA:
        errs.append('schema 应为 %s' % LEDGER_SCHEMA)
    rows = data.get('rows') if isinstance(data, dict) else None
    if not isinstance(rows, list):
        errs.append('rows 缺失或不是列表')
        rows = []
    for idx, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            errs.append('第 %d 行不是对象' % idx)
            continue
        term = str(row.get('term') or '').strip()
        doc = str(row.get('doc') or '').strip()
        d_class = str(row.get('d_class') or '').strip()
        exit_ = str(row.get('exit') or '').strip()
        evidence = str(row.get('evidence') or '').strip()
        source = str(row.get('source') or '').strip()
        reviewer = str(row.get('reviewer') or '').strip()
        tag = '第 %d 行（%s → %s）' % (idx, term or '?', doc or '?')
        if not term or not doc:
            errs.append('%s 缺 term/doc' % tag)
        if d_class not in D_CLASSES:
            errs.append('%s d_class 须为 %s 之一（现为 %r）'
                        % (tag, '/'.join(D_CLASSES), d_class))
        if exit_ not in LEDGER_EXITS:
            errs.append('%s exit 须为 %s 之一（现为 %r）'
                        % (tag, '/'.join(LEDGER_EXITS), exit_))
        if not evidence:
            errs.append('%s 缺 evidence（处置依据）' % tag)
        if d_class in ('D3', 'D4', 'D5') and not source:
            errs.append('%s D3–D5 须填 source（来源+条目/URL+日期）' % tag)
        if exit_ == 'exempt' and not reviewer:
            errs.append('%s 豁免须填 reviewer（复核人）' % tag)
    for e in errs:
        print('台账违例: %s' % e)
    print('台账 %s：%d 行，%d 处违例' % (os.path.basename(path), len(rows), len(errs)))
    return 1 if errs else 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    reg_path, docs = REGISTRY, []
    reg2_path = REGISTRY2
    pair_index_path = PAIR_INDEX
    std_index_path = STD_PAIR_INDEX
    ledger_path = ''
    injected = False
    i = 0
    while i < len(argv):
        if argv[i] == '--docs':
            docs = argv[i + 1:]
            break
        if argv[i] == '--check-ledger':
            return check_ledger(argv[i + 1] if i + 1 < len(argv) else '')
        if argv[i] == '--registry':
            reg_path, i, injected = argv[i + 1], i + 1, True
        elif argv[i] == '--registry2':
            reg2_path, i = argv[i + 1], i + 1
        elif argv[i] == '--ledger':
            ledger_path, i = argv[i + 1], i + 1
        elif argv[i] == '--pair-index':
            pair_index_path, i = argv[i + 1], i + 1
        elif argv[i] == '--std-index':
            std_index_path, i = argv[i + 1], i + 1
        i += 1
    if ledger_path and not docs:
        print('--ledger 仅在 --docs 模式可用（先给台账路径，再给 --docs <词条>…）')
        return 2
    if injected and '--registry2' not in argv:
        reg2_path = ''  # 注入单表模式：跳过人名表，保证测试密闭

    all_self_errors, warns = [], []
    doc_rows, orig_entries = [], []

    def load_one(label, path, warn_orig=True):
        full_rows, w = parse_registry_full(path)
        rows = [(t, trans, fs, basis, date, ln)
                for t, _orig, trans, fs, basis, date, ln in full_rows]
        e, dw = check_registry_self(rows)
        all_self_errors.extend('%s %s' % (label, x) for x in e)
        warns.extend('%s %s' % (label, x) for x in w + dw)
        # 非英语术语缺原文（ADR-0087：提醒，不改正、不计硬错误）：清单落 orig-missing.txt
        # 人名表按 ADR-0030（2026-11-10）豁免：来源页与工具书均未给原生文字者留「—」，不再逐行提醒
        if warn_orig:
            for term, lineno in orig_missing(full_rows):
                warns.append('非英语术语缺原文（提醒）: %s %s（行 %d）' % (label, term, lineno))
                orig_entries.append((label, term, lineno))
        doc_rows.extend(rows)
        return rows

    reg1_rows = load_one('登记册', reg_path)
    reg2_rows = load_one('人名表', reg2_path, warn_orig=False)

    # 审定引用配对检查（ADR-0088）：注入模式（测试）跳过保证密闭；索引缺失时跳过并提示；
    # --pair-index 可指定索引（测试用小索引注入，兼作集成测试入口）
    pair_bad, std_bad, lib_bad = [], [], []
    # 两个索引各自独立开合：注入模式下只有显式给出该索引才跑（测试密闭、互不拖慢）
    if (not injected or '--pair-index' in argv) and os.path.exists(pair_index_path):
        pair_index = term_pairing.load_index(pair_index_path)
        pair_bad = audit_basis_pairs(reg1_rows, pair_index)
        for term, trans, v, ln in pair_bad[:10]:
            warns.append('审定引用无配对（告警）: %s「%s」档 %s（行 %d）' % (term, trans, v, ln))
        if len(pair_bad) > 10:
            warns.append('…（其余 %d 条见清单）' % (len(pair_bad) - 10))
        # 库名如实（ADR-0088 第 2 条）：引证形与实际库别不符
        for term, _trans, _fs, basis, _d, ln in reg1_rows:
            for msg in term_pairing.audit_citation_libs(pair_index, term, basis):
                lib_bad.append((msg, ln))
        for msg, ln in lib_bad[:10]:
            warns.append('引证库名失实（告警）: %s（行 %d）' % (msg, ln))
        if len(lib_bad) > 10:
            warns.append('…（其余 %d 条见清单）' % (len(lib_bad) - 10))
    elif not injected and not os.path.exists(pair_index_path):
        print('审定引用配对检查：索引缺失，跳过（python -I tools/build_term_pair_index.py 预建）')
    if (not injected or '--std-index' in argv) and os.path.exists(std_index_path):
        std_index = term_pairing.load_index(std_index_path)
        std_bad = audit_std_pairs(reg1_rows, std_index)
        for term, trans, v, ln in std_bad[:10]:
            warns.append('标准库引用无配对（告警）: %s「%s」档 %s（行 %d）'
                         % (term, trans, v, ln))
        if len(std_bad) > 10:
            warns.append('…（其余 %d 条见清单）' % (len(std_bad) - 10))

    print('登记册 %s 行 %d | 人名表 %s 行 %d'
          % (os.path.basename(reg_path or '(跳过)'), len(reg1_rows),
             os.path.basename(reg2_path or '(跳过)'), len(reg2_rows)))
    for e in all_self_errors:
        print('自洽违例: %s' % e)
    for w in warns:
        print(w)

    if docs:
        body_cache = {}
        misses = 0
        ledger_rows = []
        for row in doc_rows:
            term, trans, first_seen = row[0], row[1], row[2]
            # 单字母碎片是「s/scholem 首译」型的字头目录前缀，不是 slug：
            # 保留会以 endswith('s.md') 误配任意 s 结尾文档（zombies 先例，
            # 119 条噪点淹没真告警；specs/036 裁定表）
            slugs = [s for s in re.split(r'[（()）/,、]', first_seen or '')
                     if s.strip() and len(s.strip()) > 1
                     and re.fullmatch(r'[a-z0-9\-]+', s.strip())]
            hit_docs = [d for d in docs
                        if any(d.endswith('%s.md' % s) or ('/%s/' % s) in d for s in slugs)]
            for d in hit_docs:
                if d not in body_cache:
                    body_cache[d] = open(os.path.join(ROOT, d), encoding='utf-8').read()
                # 落地核销两层语义（2026-10-30）：任一变体出现=已落地；
                # 有变体但主形未出现=涟漪信号（登记变更后正文待看齐）。
                vs = translations(trans)
                head = trans.split('（')[0].strip()
                found = [t for t in vs if t and t in body_cache[d]]
                if not found:
                    print('正文缺登记译法（告警）: %s 的「%s」未见于 %s'
                          % (term, '／'.join(sorted(vs)), d))
                    misses += 1
                    ledger_rows.append(_ledger_row(d, term, trans, vs, head, 'missing'))
                elif ('亦作' in trans and head and head in vs
                      and head not in found):
                    print('正文主译待对齐（涟漪）: %s 于 %s 用「%s」，主译「%s」未落地'
                          % (term, d, '／'.join(found), head))
                    ledger_rows.append(_ledger_row(d, term, trans, vs, head, 'ripple'))
        print('定点核销：%d 个文档，%d 处疑似缺译法（仅告警）' % (len(docs), misses))
        if ledger_path:
            write_ledger(ledger_path, ledger_rows, docs)
            print('判读台账骨架（D 类/出口/证据/凭证/复核人待填）: %d 行 → %s'
                  % (len(ledger_rows), ledger_path))

    hard = len(all_self_errors)
    print('硬错误 %d（自洽 %d）' % (hard, len(all_self_errors)))
    # 非英语术语缺原文（ADR-0087：提醒）：全量清单只对正式登记表落盘（注入模式=测试，不写产物）
    if not injected:
        write_orig_missing(orig_entries, ORIG_REPORT)
        print('非英语术语缺原文（提醒，不计硬错误）: %d 条，清单 → %s'
              % (len(orig_entries), ORIG_REPORT))
        # 审定引用配对（ADR-0088）：告警级，清单落 specs/058
        if pair_bad or (os.path.exists(pair_index_path) and '--pair-index' not in argv):
            write_pair_warnings(pair_bad, PAIR_REPORT)
            print('审定引用无配对（告警，不计硬错误）: %d 条，清单 → %s'
                  % (len(pair_bad), PAIR_REPORT))
        if std_bad or (os.path.exists(std_index_path) and '--std-index' not in argv):
            write_pair_warnings(std_bad, STD_PAIR_REPORT)
            print('标准库引用无配对（告警，不计硬错误）: %d 条，清单 → %s'
                  % (len(std_bad), STD_PAIR_REPORT))
        if lib_bad or os.path.exists(pair_index_path):
            write_lib_warnings(lib_bad, LIB_REPORT)
            print('引证库名失实（告警，不计硬错误）: %d 条，清单 → %s'
                  % (len(lib_bad), LIB_REPORT))
        # 术语表首现悬空（2026-11-26）：与「人名首现悬空」同口径，清单落 specs/058
        term_bad = term_dangling_first(reg1_rows)
        if not docs:
            for term, ref, ln in term_bad[:10]:
                print('术语首现悬空（告警）: %s → en/<%s>（行 %d）' % (term, ref, ln))
            if len(term_bad) > 10:
                print('…（其余 %d 条见清单）' % (len(term_bad) - 10))
        _atomic_write(TERM_FIRST_REPORT, '\n'.join(
            ['%s\t%s\t%d' % d for d in term_bad] +
            ['汇总\t%d\t术语首现悬空（ADR-0009 目录命名／补编落 supplement.html）'
             % len(term_bad)]) + '\n')
        print('术语首现悬空（告警，不计硬错误）: %d 条，清单 → %s'
              % (len(term_bad), TERM_FIRST_REPORT))
        # 人名缺籍属/生卒（013 工程）：同口径告警，清单落 specs/013
        if reg2_path:
            rows2, _w2 = parse_registry2_full(reg2_path)
            person_entries = person_missing(rows2)
            person_terminal, terminal_by_src = person_terminal_stats(rows2)
            terminal_index = os.path.join(
                ROOT, 'specs', '013-person-attribution', 'results',
                'person-terminal-2026-11-26.tsv')
            write_person_terminal_index(rows2, terminal_index)
            if not docs:
                for term, lineno, lack in person_entries[:22]:
                    print('人名缺%s（告警）: %s（行 %d）' % (lack, term, lineno))
                if len(person_entries) > 22:
                    print('…（其余 %d 条见清单）' % (len(person_entries) - 22))
            write_person_missing(person_entries, PERSON_REPORT, person_terminal)
            print('人名缺籍属/生卒（告警，不计硬错误）: %d 条（已判终态 %d 条未计入：'
                  '依据列 %d／013 台账 %d），清单 → %s'
                  % (len(person_entries), person_terminal,
                     terminal_by_src.get('basis', 0),
                     person_terminal - terminal_by_src.get('basis', 0),
                     PERSON_REPORT))
            dangling, informal = person_dangling_first(rows2)
            if not docs:
                for term, slug, ln, _c in dangling[:10]:
                    print('人名首现悬空（告警）: %s → en/%s（行 %d）' % (term, slug, ln))
                if len(dangling) > 10:
                    print('…（其余 %d 条见清单）' % (len(dangling) - 10))
                for term, val, ln, canon in informal[:5]:
                    print('人名首现非规范形（告警）: %s → %s（应为 %s，行 %d）'
                          % (term, val, canon, ln))
                if len(informal) > 5:
                    print('…（其余 %d 条见清单）' % (len(informal) - 5))
            _atomic_write(PERSON_FIRST_REPORT, '\n'.join(
                ['%s\t%s\t%d\t%s' % d for d in dangling] +
                ['汇总\t%d\t人名首现悬空（ADR-0009 目录命名）' % len(dangling)] +
                ['%s\t%s\t%d\t应为 %s' % d for d in informal] +
                ['汇总\t%d\t人名首现非规范形（<letter>/<slug>，宜归一裸 slug）'
                 % len(informal)]) + '\n')
            print('人名首现悬空（告警，不计硬错误）: %d 条；非规范形: %d 条，清单 → %s'
                  % (len(dangling), len(informal), PERSON_FIRST_REPORT))
    if docs:
        return 0
    return 1 if hard else 0


if __name__ == '__main__':
    sys.exit(main())

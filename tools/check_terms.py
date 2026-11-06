# -*- coding: utf-8 -*-
"""术语一致性检查器（specs/002 FR-001..005；ADR-0012/specs/008 扩展三表）。

用法:
  python tools/check_terms.py                       # 三表冲突 + 两登记册自洽（门禁）
  python tools/check_terms.py --docs a/某词条.md …   # 定点核销：登记册"首现"驱动的正文核对
  python tools/check_terms.py --registry <路径> --glossary <路径>   # 测试注入（单表模式）
  python tools/check_terms.py --registry2 <路径>    # 注入第二登记册（人名表）

三表:
  - 术语登记册 yi-zhe-shuo-ming.md（键|原文|译法|出处|依据|日期，六列；
    旧五列「键|译法|首现|依据|裁定日期」按旧口径兼容解析）
  - 人名登记册 ren-ming-biao.md（同六列，ADR-0012 自术语表拆出）
  - 发布词汇表 qian-yan/ci-hui-biao.md（英语|中文|备注，发布视图）

规则:
  - 键规范化：剥 * 斜体标记、去首尾空格、比对用 casefold，展示保留原样。
  - 译法集合：取"（"前主形，并按 / 与 ／ 拆分为变体；两侧集合互斥 = 冲突（硬错误）；
    一侧为另一侧真子集 = 词汇表滞后（告警）。
  - 登记册自洽：废弃行须有同键非废弃行；裁定日期缺失、依据列缺失 = 告警
    （数据欠账，登记会话补齐）；同键同译法重复 = 硬错误。
  - 非英语术语缺原文 = 告警（非硬错误，2026-11-06）：键含非 ASCII 拉丁变音符／
    非拉丁文字，或命中内置小语种词表者，「原文」列为「—」或空（旧五列无该列
    亦视为缺）即记一条；全量清单落 specs/008 results/orig-missing.txt。
退出码: 0 无硬错误；1 有冲突或自洽违例（--docs 模式仅告警，恒 0）。
"""
import io
import os
import re
import sys
from collections import defaultdict

_enc = getattr(sys.stdout, 'encoding', None)
if not _enc or _enc.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, 'yi-zhe-shuo-ming.md')
REGISTRY2 = os.path.join(ROOT, 'ren-ming-biao.md')
GLOSSARY = os.path.join(ROOT, 'qian-yan', 'ci-hui-biao.md')
ORIG_REPORT = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                           'orig-missing.txt')
DEPRECATED_MARK = '已废弃'
HEADER_WORDS = {'原文', '译法', '首现', '依据', '裁定日期', '人名', '文献',
                '条目', 'term', '原文形态', '通行中文', '键', '出处', '日期'}

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



def norm_key(text):
    """术语键：剥斜体标记与空白、变音符折叠（ADR-0013 同人归并）、casefold 比对。"""
    import unicodedata
    s = unicodedata.normalize('NFD', text.replace('*', '').strip())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s).casefold()


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


def split_row(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def is_data_row(cells):
    # 只校验首列：六列新格式的第二列（原文）允许为空/「—」，不能据此丢弃数据行
    return (len(cells) >= 2 and cells[0]
            and cells[0].casefold() not in HEADER_WORDS
            and not set(cells[0]) <= set(':-— '))


def parse_registry_full(path):
    """返回 rows=[(term, orig, trans, first_seen, basis, date, lineno)] 与解析告警。

    六列（键|原文|译法|出处|依据|日期，2026-11-06 原文列迁移）为标准格式；
    旧五列（原文|译法|首现|依据|裁定日期）与旧四列（无依据）按旧口径解析并容忍，
    此时 orig=None 表示「旧格式没有原文列」（区别于新格式的留空或填「—」）。
    """
    rows, warns = [], []
    if not path or not os.path.exists(path):
        return rows, warns
    for lineno, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.startswith('|'):
            continue
        cells = split_row(line)
        if not is_data_row(cells):
            continue
        n = len(cells)
        if n >= 6:
            term, orig, trans = cells[0], cells[1], cells[2]
            first_seen, basis, date = cells[3], cells[4], cells[5]
            if n > 6:
                warns.append('第 %d 行 %d 列（应为 6，已取前 6 列）：%s'
                             % (lineno, n, term))
            if not basis:
                warns.append('缺依据列（告警）：%s（第 %d 行）' % (term, lineno))
        else:
            term, orig, trans = cells[0], None, cells[1]
            first_seen = cells[2] if n >= 3 else ''
            if n >= 5:
                basis, date = cells[3], cells[4]
                if not basis:
                    warns.append('缺依据列（告警）：%s（第 %d 行）'
                                 % (term, lineno))
            elif n == 4:
                basis, date = '', cells[3]
                warns.append('缺依据列（告警）：%s（第 %d 行）' % (term, lineno))
            else:
                basis, date = '', ''
                warns.append('第 %d 行仅 %d 列（应为 5）：%s'
                             % (lineno, n, term))
        rows.append((term, orig, trans, first_seen, basis, date, lineno))
    return rows, warns


def parse_registry(path):
    """兼容旧签名：rows=[(term, trans, first_seen, basis, date, lineno)]。

    列位解析见 parse_registry_full（六列标准格式 + 旧五/四列兼容）。
    """
    full, warns = parse_registry_full(path)
    return [(t, trans, fs, basis, date, ln)
            for t, _orig, trans, fs, basis, date, ln in full], warns


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


def orig_missing(rows):
    """「非英语术语缺原文」：rows 为 parse_registry_full 口径，返回 [(键, 行号)]。

    原文列为「—」或空即记；旧五/四列格式无原文列（orig=None），迁移未完成的
    行同样计入（本告警即迁移清单）。
    """
    out = []
    for term, orig, _trans, _fs, _basis, _date, lineno in rows:
        if orig is not None and orig.strip() not in ORIG_BLANK:
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
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    os.replace(tmp, path)


def parse_glossary(path):
    """返回 rows=[(term, trans, lineno)] 与解析告警。

    译法集合取第 2 列，并从第 3 列注记提取 亦作"X" 形态并入
    （整列并入会把叙述文字当译法，008 战役口径 2026-10-29 收窄）。
    """
    rows, warns = [], []
    for lineno, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.startswith('|'):
            continue
        cells = split_row(line)
        if not is_data_row(cells):
            continue
        trans = cells[1]
        if len(cells) >= 3:
            # 第 3 列注记变体提取：前缀词含亦作/译作/亦译/亦音译/音译/又译/又作，
            # 连排引号（"X""Y"）逐个吸收（与登记册 translations 口径对齐 2026-11-03）
            extra = []
            for m in re.finditer(
                    r'(?:亦作|译作|亦译|亦音译|音译|又译|又作)[“"]([^”"]{1,40})[”"]', cells[2]):
                for v in re.split(r'[/／；、;，]', m.group(1)):
                    if v.strip():
                        extra.append(v.strip())
                rest = cells[2][m.end():]
                while True:
                    m2 = re.match(r'[“"]([^”"]{1,40})[”"]', rest.strip())
                    if not m2:
                        break
                    for v in re.split(r'[/／；、;，]', m2.group(1)):
                        if v.strip():
                            extra.append(v.strip())
                    rest = rest.strip()[m2.end():]
            if extra:
                trans += '；' + '；'.join(extra)
        rows.append((cells[0], trans, lineno))
    return rows, warns


def collect(rows):
    """key -> {translation_set, display_key, linenos}"""
    table = {}
    for row in rows:
        term, trans, lineno = row[0], row[1], row[-1]
        key = norm_key(term)
        entry = table.setdefault(key, {'key': key, 'display': term,
                                       'trans': set(), 'lines': []})
        entry['trans'] |= translations(trans)
        entry['lines'].append(lineno)
    return table


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


def check_conflicts(reg, glos, label):
    """登记册↔词汇表：互斥 = 冲突（硬错误）；词汇表缺登记侧变体 = 滞后（告警）。
    词汇表多出的变体不报（发布视图允许含更宽通行变体，2026-11-03 口径收窄）。"""
    conflicts, lagging = [], []
    for key in sorted(set(reg) & set(glos)):
        rt, gt = reg[key]['trans'], glos[key]['trans']
        if rt and gt and not (rt & gt):
            conflicts.append((label, reg[key]['display'], sorted(rt), sorted(gt),
                              reg[key]['lines'], glos[key]['lines']))
        elif rt and gt and (gt < rt):
            lagging.append((label, reg[key]['display'], sorted(rt), sorted(gt)))
    return conflicts, lagging


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    reg_path, glos_path, docs = REGISTRY, GLOSSARY, []
    reg2_path = REGISTRY2
    injected = False
    i = 0
    while i < len(argv):
        if argv[i] == '--docs':
            docs = argv[i + 1:]
            break
        if argv[i] == '--registry':
            reg_path, i, injected = argv[i + 1], i + 1, True
        elif argv[i] == '--registry2':
            reg2_path, i = argv[i + 1], i + 1
        elif argv[i] == '--glossary':
            glos_path, i = argv[i + 1], i + 1
        i += 1
    if injected and '--registry2' not in argv:
        reg2_path = ''  # 注入单表模式：跳过人名表，保证测试密闭

    conflicts, lagging = [], []
    all_self_errors, warns = [], []
    doc_rows, orig_entries = [], []

    def load_one(label, path):
        full_rows, w = parse_registry_full(path)
        rows = [(t, trans, fs, basis, date, ln)
                for t, _orig, trans, fs, basis, date, ln in full_rows]
        reg = collect(rows)
        c, l = check_conflicts(reg, glos, label)
        conflicts.extend(c)
        lagging.extend(l)
        e, dw = check_registry_self(rows)
        all_self_errors.extend('%s %s' % (label, x) for x in e)
        warns.extend('%s %s' % (label, x) for x in w + dw)
        # 非英语术语缺原文（只告警，不改正、不计硬错误）：清单落 orig-missing.txt
        for term, lineno in orig_missing(full_rows):
            warns.append('非英语术语缺原文: %s %s（行 %d）' % (label, term, lineno))
            orig_entries.append((label, term, lineno))
        doc_rows.extend(rows)
        return rows, reg

    glos_rows, glos_warns = parse_glossary(glos_path)
    glos = collect(glos_rows)
    reg1_rows, reg1 = load_one('登记册', reg_path)
    reg2_rows, reg2 = load_one('人名表', reg2_path)

    print('登记册 %s 行 %d（键 %d） | 人名表 %s 行 %d（键 %d） | 词汇表行 %d（键 %d） | 交集键 %d+%d'
          % (os.path.basename(reg_path or '(跳过)'), len(reg1_rows), len(reg1),
             os.path.basename(reg2_path or '(跳过)'), len(reg2_rows), len(reg2),
             len(glos_rows), len(glos),
             len(set(reg1) & set(glos)), len(set(reg2) & set(glos))))
    for w in glos_warns:
        print('告警(解析): %s' % w)
    for label, term, rt, gt, rl, gl in conflicts:
        print('冲突: %s\n  %s(第%s行): %s\n  词汇表(第%s行): %s'
              % (term, label, ','.join(map(str, rl)), '、'.join(rt),
                 ','.join(map(str, gl)), '、'.join(gt)))
    for label, term, rt, gt in lagging:
        print('词汇表滞后（告警）: [%s] %s | 登记侧: %s | 词汇表: %s'
              % (label, term, '、'.join(rt), '、'.join(gt)))
    for e in all_self_errors:
        print('自洽违例: %s' % e)
    for w in warns:
        print(w)

    if docs:
        body_cache = {}
        misses = 0
        for row in doc_rows:
            term, trans, first_seen = row[0], row[1], row[2]
            slugs = [s for s in re.split(r'[（()）/,、]', first_seen or '')
                     if s.strip() and re.fullmatch(r'[a-z0-9\-]+', s.strip())]
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
                elif ('亦作' in trans and head and head in vs
                      and head not in found):
                    print('正文主译待对齐（涟漪）: %s 于 %s 用「%s」，主译「%s」未落地'
                          % (term, d, '／'.join(found), head))
        print('定点核销：%d 个文档，%d 处疑似缺译法（仅告警）' % (len(docs), misses))

    hard = len(conflicts) + len(all_self_errors)
    print('硬错误 %d（冲突 %d + 自洽 %d），词汇表滞后 %d'
          % (hard, len(conflicts), len(all_self_errors), len(lagging)))
    # 非英语术语缺原文：全量清单只对正式登记表落盘（注入模式=测试，不写产物）
    if not injected:
        write_orig_missing(orig_entries, ORIG_REPORT)
        print('非英语术语缺原文（告警，不计硬错误）: %d 条，清单 → %s'
              % (len(orig_entries), ORIG_REPORT))
    if docs:
        return 0
    return 1 if hard else 0


if __name__ == '__main__':
    sys.exit(main())

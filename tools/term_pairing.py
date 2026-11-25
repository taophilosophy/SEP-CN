# -*- coding: utf-8 -*-
"""审定引用配对判据的共享实现（ADR-0088，2026-11-26）。

背景与判据见 `rules/adr/0088-术语在线审定引用须配对.md`：termonline-all 通道回的是
模糊匹配，缓存「有同形中文」不构成「审定命中」；须按 英文折叠形＝键 且 中文＝译法形
的配对判据验证，库名（审定公布／海峡两岸／标准文件／其他）如实区分。

本模块是唯一实现，供三处共用：
  * `tools/build_term_pair_index.py` —— 从 24k 份缓存预建条目索引（gz 落盘）；
  * `tools/check_terms.py` —— 审定引用配对检查（告警）；
  * `specs/058-term-full-reextraction/bin/audit_fuzzy_basis.py` —— 全量批量审计。
"""
import gzip
import json
import re
import unicodedata
from collections import defaultdict

# 索引产物路径（入库；缓存新增后重跑 builder 刷新）
INDEX_PATH = 'specs/058-term-full-reextraction/results/term-pair-index.json.gz'
STD_INDEX_PATH = 'specs/058-term-full-reextraction/results/std-pair-index.json.gz'
QD = 'specs/008-terminology-campaign/results/queries/termonline-all'
STD_QD = 'specs/008-terminology-campaign/results/queries/termonline-standard'

# 库别标记（lib_of 的返回值）
LIB_AUDIT = 'audit'      # 审定公布名词库
LIB_TW = 'tw'            # 海峡两岸名词对照库
LIB_STD = 'std'          # 标准文件术语库
LIB_OTHER = 'other'      # 其他来源数据库（百科／辞典等）


def strong(s):
    """折叠形：剥属格 's、去变音符、小写，只留拉丁字母数字与 CJK。"""
    s = re.sub(r"['’][sS]?\b", '', str(s or ''))
    s = unicodedata.normalize('NFKD', s.casefold())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', s)


def en_stems(s):
    """英文各义项（分号／逗号分隔）的折叠形与去复数形，-ise/-ize、-our/-or 互认。"""
    out = set()
    for part in re.split(r'[;,]', str(s or '')):
        t = strong(part)
        if len(t) < 3:
            continue
        forms = {t}
        for a, b in (('ise', 'ize'), ('isation', 'ization'), ('our', 'or')):
            if a in t:
                forms.add(t.replace(a, b))
            if b in t:
                forms.add(t.replace(b, a))
        for suf, rep in (('ies', 'y'), ('ses', 's'), ('es', ''), ('s', '')):
            if t.endswith(suf) and len(t) > len(suf) + 2:
                forms.add(t[:-len(suf)] + rep)
        out |= {x for x in forms if len(x) >= 3}
    return out


def cn_keys(s):
    """中文形归一：GB 方括号是可选字（优先[方]法＝优先法／优先方法），两种都收；括注剥离。"""
    base = re.sub(r'（[^）]*）|\([^)]*\)', '', str(s or ''))
    out = {strong(re.sub(r'\[[^\]]*\]', '', base)),
           strong(re.sub(r'\[([^\]]*)\]', r'\1', base))}
    return {x for x in out if x}


def zh_forms(zh, *extra):
    """登记行内出现过的中文形集合：译法各形（分号／顿号／斜线分隔）＋所有引号内中文形
    ＋「审定…作／＝X」的 X。

    多形译法必须拆开：`构造主义；建构主义` 整串归一会归一成一串无意义字符，与审定
    “构造主义”永远配不上（2026-11-26 实测：constructivism 因此假告警）。"""
    raw = re.sub(r'（[^）]*）|\([^)]*\)', '', str(zh or ''))
    forms = set()
    for part in re.split(r'[；;、／/|]', raw):
        p = part.strip(' 《》\u3000')
        if p:
            forms |= cn_keys(p)
    joined = ' '.join((zh,) + tuple(extra or ()))
    for x in re.findall(r'[“"]([^”"]{1,14})[”"]', joined):
        if re.search(r'[一-鿿]', x):
            forms |= cn_keys(x)
    for x in re.findall(r'审定[^；。，]{0,16}?[＝作]([一-鿿]{2,10})', joined):
        forms |= cn_keys(x)
    return forms


def lib_of(std):
    """来源名→库别；未知非空来源一律视为审定公布（历史缓存默认）。"""
    s = str(std or '')
    if not s:
        return None
    if '海峡两岸' in s:
        return LIB_TW
    if '国家标准' in s or '标准文件' in s:
        return LIB_STD
    if '百科' in s or '辞典' in s or '维基' in s or '传播工程' in s:
        return LIB_OTHER
    return LIB_AUDIT


def cache_filename(key):
    """缓存文件名推导（与 cnki_query.safe_key 同式：非字母数字折下划线）。"""
    return re.sub(r'[^0-9a-zA-Z]+', '_', str(key).strip().lower()).strip('_')


def build_index(qd=QD, files=None, force_lib=None):
    """扫描缓存目录建索引。返回 {records, by_key, en, cn}；records 元素为
    [cn, en, std, code, lib]，三个映射的值都是 records 下标列表。"""
    import glob
    import io
    import os
    if files is None:
        files = sorted(glob.glob(os.path.join(qd, '*.json')))
    records = []
    rec_ids = {}
    by_key, en_idx, cn_idx = defaultdict(list), defaultdict(list), defaultdict(list)
    for p in files:
        key = os.path.basename(p)[:-5]
        try:
            j = json.load(io.open(p, encoding='utf-8'))
        except Exception:
            continue
        for h in j.get('hits') or []:
            std = str(h.get('standard') or h.get('source') or '')
            lib = force_lib or lib_of(std)
            if not lib:
                continue
            rec = [h.get('cn') or '', h.get('en') or '', std,
                   h.get('code') or h.get('wordNumber') or '', lib]
            sig = (rec[0], rec[1], rec[2], rec[3], rec[4])
            rid = rec_ids.get(sig)
            if rid is None:
                rid = len(records)
                rec_ids[sig] = rid
                records.append(rec)
            by_key[key].append(rid)
            for e in en_stems(rec[1]):
                en_idx[e].append(rid)
            for ck in cn_keys(rec[0]):
                cn_idx[ck].append(rid)
    return {'records': records, 'by_key': dict(by_key),
            'en': dict(en_idx), 'cn': dict(cn_idx)}


def save_index(index, path=INDEX_PATH):
    payload = json.dumps(index, ensure_ascii=False,
                         separators=(',', ':')).encode('utf-8')
    with gzip.open(path, 'wb', compresslevel=9) as f:
        f.write(payload)
    return len(payload)


def load_index(path=INDEX_PATH):
    with gzip.open(path, 'rb') as f:
        return json.loads(f.read().decode('utf-8'))


def classify_std_row(key, zh, basis, index):
    """标准文件术语库（GB 标准）配对判定：同 classify_row，但条目全按标准库计。
    返回 (verdict, hit)；verdict ∈ pair/en-only/cn-only/none。"""
    forms = zh_forms(zh, basis)
    seg = re.split(r'\s*/\s*', key)
    stems = set()
    for s in [key] + seg:
        stems |= en_stems(s)
    records = index['records']
    pool_ids = set()
    for s in [key] + seg:
        pool_ids.update(index['by_key'].get(cache_filename(s), ()))
    for e in stems:
        pool_ids.update(index['en'].get(e, ()))
    for f in forms:
        pool_ids.update(index['cn'].get(f, ()))
    pool = [records[i] for i in pool_ids]
    en_hits = [r for r in pool if en_stems(r[1]) & stems]
    cn_hits = [r for r in pool if cn_keys(r[0]) & forms]
    pairs = [r for r in en_hits if cn_keys(r[0]) & forms]
    if pairs:
        return 'pair', pairs[0]
    if en_hits:
        return 'en-only', en_hits[0]
    if cn_hits:
        return 'cn-only', cn_hits[0]
    return 'none', ['', '', '', '', '']


def needs_std_pairing(basis):
    """依据是否主张 GB 标准库命中且未说明（true = 需配对否则告警）。"""
    if 'GB 标准库' not in basis and 'termonline-standard' not in basis:
        return False
    if ('无收录' in basis or '查无' in basis or '无配对' in basis
            or '无直接对应' in basis or '无该键配对条目' in basis):
        return False
    if explicit_citation(basis) or ACK_RE.search(basis):
        return False
    return True


def classify_row(key, zh, basis, index):
    """单行判定。返回 (verdict, hit)；verdict ∈ pair/en-only/cn-only/tw-only/none，
    hit 为 [cn, en, std, code, lib]（none 时空表）。判据同 ADR-0088。"""
    forms = zh_forms(zh, basis)
    seg = re.split(r'\s*/\s*', key)
    stems = set()
    for s in [key] + seg:
        stems |= en_stems(s)
    records = index['records']
    pool_ids = set()
    for s in [key] + seg:
        pool_ids.update(index['by_key'].get(cache_filename(s), ()))
    for e in stems:
        pool_ids.update(index['en'].get(e, ()))
    for f in forms:
        pool_ids.update(index['cn'].get(f, ()))
    audit_pool = [records[i] for i in pool_ids if records[i][4] == LIB_AUDIT]
    en_hits = [r for r in audit_pool if en_stems(r[1]) & stems]
    cn_hits = [r for r in audit_pool if cn_keys(r[0]) & forms]
    pairs = [r for r in en_hits if cn_keys(r[0]) & forms]
    tw = [records[i] for i in pool_ids if records[i][4] == LIB_TW
          and (en_stems(records[i][1]) & stems or cn_keys(records[i][0]) & forms)]
    if pairs:
        return 'pair', pairs[0]
    if en_hits:
        return 'en-only', en_hits[0]
    if cn_hits:
        return 'cn-only', cn_hits[0]
    if tw:
        return 'tw-only', tw[0]
    return 'none', ['', '', '', '', '']


# 「行内已说明」判据：依据列含这些措辞即视为已交代与审定形／库别的关系或无对口，
# 不再要求配对（与 specs/058 批 41–53 清账口径一致）。
#
# 只收精确短语，不收单字与泛词：旧表收“义”“异”“作“”“复核”，实测在 3,008 条审定
# 断言里把“义务论”“差异”“亦作“”“审定库复核一致”全豁免掉了，等于门禁形同虚设
# （2026-11-26 量测：旧表 0 告警，精确表 38 条真缺口）。
ACK_RE = re.compile(
    # 否定／无对口
    r'不采|不收录|无收录|仅收|无相关|无对口|无直接|无查询件|无精确命中|无命中|无裸词|'
    r'无“|无独立|未收|查无|0 条|未见|非本词|命中他义|非审定|无该条|'
    # 库别说明
    r'对照库|其他来源|不一致|'
    # 形异／义异／英文侧交代
    r'义近|异义|异形|形异|同形异|异构形|异拼|异序|异概念|分义|'
    r'英文对|英文列作|通名|相邻形|全称形|形容词形|直接命中|同名噪声|同形噪声|噪声命中|'
    # 判定与处置记录
    r'佐证|撞形|降为亦作|审定形|《数学名词》形|非哲学义|语序|并行|分立|复数形|省略|'
    r'缩略|本行为|研判|同族|核心词|复合|简称|上限|豁免|本库首译|首译|收“|有“|'
    r'定名系|定名裁定|对照形')

# 「声明有命中」的反证措辞：出现即视为否定句／无对口句，不要求配对。
# 「无该键配对条目」是 ADR-0089 的标准写法（首屏无配对），必须计入负证。
NEG_RE = re.compile(
    r'无相关|无对口|未收|查无|无命中|0 条|未见|无“|无独立|不收录|仅收|非本词|命中他义|'
    r'非审定|对照库|其他来源|不一致|无该键配对条目|无配对条目')


def explicit_citation(text):
    """行内是否引出了审定的具体形：同一分段里同时出现“审定”与 作“／＝ 即算交代清楚。

    按分号分段判，不作全文匹配——否则一段里的“亦作“X””会把另一段的裸断言一起豁免掉。
    引了形即视为已交代关系（形异、义异、英文侧不同都由文字自证），未引形的裸断言才告警。"""
    for seg in re.split(r'[；;]', str(text or '')):
        if '审定' in seg and ('作“' in seg or '＝' in seg):
            return True
    return False


def claim_text(trans, basis):
    """待判文本：默认只看依据列；译法列自身写有“审定…”时才并入。

    译法列普遍含“亦作“X””，整串并入会让“作“”撞出豁免；只在译法列自己引了审定时并入。"""
    t, b = str(trans or ''), str(basis or '')
    return '%s；%s' % (t, b) if '审定' in t else b


# ---- 库名如实检查（ADR-0088 第 2 条）-------------------------------------------
#
# 形如「审定名词库（termonline-all·地理学…）作“反本质论”」的引证把库名写进了文字，
# 可以机检：所引中文形在索引里只存在于海峡两岸／其他库时，该“审定”即失实。
# 注意三类噪声：`亦作“X”` 不是引证；带条文号（01.0125）的多为纸质审定本引证，索引
# 未必覆盖；同段又称审定又称对照库的属混标（2026-11-26 实测各有命中）。
CITE_CN_RE = re.compile(r'(?<!亦)作“([^”]{1,30})”')
OTHER_MARKS = ('中华思想文化术语传播工程', '其他术语库', '百科', '维基', '辞典')
TW_MARKS = ('海峡两岸', '对照库')
CODE_RE = re.compile(r'\d{2}\.\d{3,4}')
LIB_MIXED = 'mixed'


def citation_claims(text):
    """显式引证清单 [(声称库别, 所引中文形, 前文窗口, 是否带条文号)]；无声称库别的跳过。

    窗口取「作“」之前、且不超过最近分号」——一句里的“审定作 X”不该管到下一句的
    “对照库作 Y”，否则并列两句必被判混标。"""
    t = str(text or '')
    out = []
    for m in CITE_CN_RE.finditer(t):
        cn = m.group(1)
        if not re.search(r'[一-鿿]', cn):
            continue
        sep = max(t.rfind('；', 0, m.start()), t.rfind(';', 0, m.start()))
        w = t[(sep + 1 if sep >= 0 else 0):m.start()][-90:]
        audit = '审定' in w and '非审定' not in w
        tw = any(x in w for x in TW_MARKS)
        other = any(x in w for x in OTHER_MARKS)
        if audit and (tw or other):
            lib = LIB_MIXED
        elif audit:
            lib = LIB_AUDIT
        elif tw:
            lib = LIB_TW
        elif other:
            lib = LIB_OTHER
        else:
            continue
        out.append((lib, cn, w[-46:], bool(CODE_RE.search(w))))
    return out


def audit_citation_libs(index, key, basis):
    """库名如实检查：返回问题描述列表（空＝无问题）。"""
    recs = index['records']
    bad = []
    for lib, cn, _ctx, coded in citation_claims(basis):
        if coded and lib != LIB_MIXED:
            continue
        ids = set()
        for k in cn_keys(cn):
            ids.update(index['cn'].get(k, ()))
        if not ids:
            continue
        libs = {recs[i][4] for i in ids}
        if lib == LIB_MIXED:
            bad.append('%s：同段既称审定又称对照库／其他库（引“%s”）' % (key, cn))
        elif lib not in libs:
            bad.append('%s：引“%s”作%s，索引内只见%s'
                       % (key, cn, lib, '／'.join(sorted(libs))))
    return bad


def needs_pairing(basis):
    """该依据是否主张审定命中且未说明（true = 需要配对否则告警）。"""
    if '审定' not in basis:
        return False
    if explicit_citation(basis):
        return False
    if ACK_RE.search(basis):
        return False
    return True

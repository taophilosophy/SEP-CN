# -*- coding: utf-8 -*-
"""jaina-philosophy 重译批登记（2026-11-25）：术语 55、典籍 24、人物 4。幂等。
依据栏不写检索凭证（本轮检索通道不可用）；典籍汉名沿用既有作者行已立形（《论存在者》《一切义成就》等）。"""
import io
import re
import sys
import unicodedata

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key  # noqa: E402

DATE = '2026-11-25'


def _skey(s):
    s = unicodedata.normalize('NFKD', s)
    return ''.join(ch for ch in s if not unicodedata.combining(ch)).lower()


def insert_sorted(lines, sec_title, row_key, row, keycol=0):
    ini = lines.index('## ' + sec_title)
    nxt = len(lines)
    for j in range(ini + 1, len(lines)):
        if lines[j].startswith('## '):
            nxt = j
            break
    pos = nxt
    for j in range(ini + 1, nxt):
        if not lines[j].startswith('| ') or lines[j].startswith('| 键') or lines[j].startswith('| 原文'):
            continue
        c = lines[j].split('|')
        if len(c) < 2:
            continue
        if _skey(c[1].strip()) > _skey(row_key):
            pos = j
            break
    lines.insert(pos, row)
    return lines


def exists(lines, key, keycol=0):
    k = norm_key(key)
    for l in lines:
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) < 2:
            continue
        if norm_key(c[keycol]) == k:
            return True
        for part in re.split(r'[;、/]', c[keycol]):
            if part.strip() and norm_key(part.strip()) == k:
                return True
    return False


def add_term(lines, key, orig, zh, first, basis):
    if exists(lines, key):
        print('跳过', key)
        return
    row = '| %s | %s | %s | %s | %s | %s |' % (key, orig, zh, first, basis, DATE)
    base = ''.join(ch for ch in unicodedata.normalize('NFKD', key[0]) if not unicodedata.combining(ch)).upper()
    sec = base if base.isalpha() and base.isascii() else '#'
    insert_sorted(lines, sec, key, row, keycol=0)
    print('登记', sec, key)


def add_person(lines, orig, alias, zh, region, life, first, basis):
    if exists(lines, orig):
        print('跳过', orig)
        return
    row = '| %s | %s | %s | %s | %s | %s | %s | %s |' % (orig, alias, zh, region, life, first, basis, DATE)
    insert_sorted(lines, orig[0].upper(), orig, row, keycol=0)
    print('登记', orig[0].upper(), orig)


TERMS = [
    ('kevala', 'केवल', '全知（kevala）', 'jaina-philosophy', '耆那教研究通行（kevala-jñāna 全知；本库统一形“全知”）'),
    ('kevalin', 'केवलिन्', '全知者', 'jaina-philosophy', '随 kevala'),
    ('syādvāda', 'स्याद्वाद', '或然论', 'jaina-philosophy', '印度哲学史学界通行（syāt 或许＋vāda 论）'),
    ('saptabhaṅgī', 'सप्तभङ्गी', '七支论法', 'jaina-philosophy', '因明与耆那逻辑通行译名'),
    ('syāt', 'स्यात्', '或许', 'jaina-philosophy', '或然论判断词义译（“或许如此”）'),
    ('avaktavya', 'अवक्तव्य', '不可言说', 'jaina-philosophy', '义译（七支之一）'),
    ('naya', 'नय', '视角', 'jaina-philosophy', '随既有 nayavāda＝诸视角说'),
    ('nikṣepa', 'निक्षेप', '安立（界定）', 'jaina-philosophy', '耆那认识论义译（多角度安立对象）'),
    ('tapas', 'तपस्', '苦行', 'jaina-philosophy', '印度宗教通行'),
    ('mahāvrata', 'महाव्रत', '大誓', 'jaina-philosophy', '耆那戒律通行（出家五誓）'),
    ('aṇuvrata', 'अणुव्रत', '小誓', 'jaina-philosophy', '耆那戒律通行（在家五戒）'),
    ('karmic matter', '—', '业质', 'jaina-philosophy', '义译（karma-pudgala，业之物质）'),
    ('mohanīya', 'मोहनीय', '惑业', 'jaina-philosophy', '耆那业论汉译通行（八业之一）'),
    ('jñāna-avaraṇīya', 'ज्ञानावरणीय', '覆智业', 'jaina-philosophy', '耆那业论义译（覆障智之业）'),
    ('darśanāvaraṇīya', 'दर्शनावरणीय', '覆见业', 'jaina-philosophy', '耆那业论义译'),
    ('antarāya', 'अन्तराय', '障碍业', 'jaina-philosophy', '耆那业论通行（障蔽能量之业）'),
    ('vedanīya', 'वेदनीय', '受业', 'jaina-philosophy', '耆那业论汉译（感苦乐之业）'),
    ('nāman', 'नामन्', '名业', 'jaina-philosophy', '耆那业论汉译（定转生种类之业）'),
    ('āyus', 'आयुस्', '寿业', 'jaina-philosophy', '耆那业论汉译（定寿命之业）'),
    ('gotra', 'गोत्र', '族业', 'jaina-philosophy', '耆那业论汉译（定种姓地位之业）'),
    ('ghātiyā', 'घातिया', '障业（有覆业）', 'jaina-philosophy', '耆那业论通行（障蔽自性之四业）'),
    ('aghātiyā', 'अघातिया', '非障业（无覆业）', 'jaina-philosophy', '耆那业论通行（不障自性之四业）'),
    ('lesyā', 'लेश्या', '业染', 'jaina-philosophy', '耆那教义译（心为业所染之色）'),
    ('gati', 'गति', '趣（转生）', 'jaina-philosophy', '印度宗教通行（四趣转生）'),
    ('upayoga', 'उपयोग', '觉用', 'jaina-philosophy', '耆那教自我定义语（经验的觉知活动），本库自拟义译'),
    ('mithyātva', 'मिथ्यात्व', '邪见', 'jaina-philosophy', '耆那教通行（三宝之反）'),
    ('mithyādarśana', 'मिथ्यादर्शन', '邪见（错误见）', 'jaina-philosophy', '随 mithyātva'),
    ('samyak darśana', 'सम्यक् दर्शन', '正见', 'jaina-philosophy', '耆那三宝通行译法（与 samyak carita 正行并行）'),
    ('samyak jñāna', 'सम्यक् ज्ञान', '正智', 'jaina-philosophy', '耆那三宝通行译法'),
    ('puṇya', 'पुण्य', '福（善业）', 'jaina-philosophy', '印度宗教通行；耆那教与 pāpa 对举'),
    ('pāpa', 'पाप', '罪（恶业）', 'jaina-philosophy', '随 puṇya'),
    ('āgama', 'आगम', '圣典（阿含）', 'jaina-philosophy', '耆那教通行（白衣派 canon 称 āgama）'),
    ('scripture', '—', '圣典', 'jaina-philosophy', '通行'),
    ('authoritative teaching', '—', '可信教说', 'jaina-philosophy', '随既有 āpta＝可信者'),
    ('testimonial cognition', '—', '证言认知', 'jaina-philosophy', '知识论通行（śabda／āpta 教说所生知）'),
    ('non-violence', '—', '非暴力', 'jaina-philosophy', '通行；与 ahiṃsā＝不害 互见'),
    ('renunciation', '—', '出离', 'jaina-philosophy', '印度宗教通行（出家弃世）'),
    ('rebirth', '—', '再生', 'jaina-philosophy', '通行'),
    ('asceticism', '—', '苦行主义', 'jaina-philosophy', '通行'),
    ('cosmic cycle', '—', '宇宙周期', 'jaina-philosophy', '耆那宇宙论通行（升降各六期）'),
    ('island-continent', '—', '洲', 'jaina-philosophy', '耆那宇宙论义译（dvīpa）'),
    ('Jambūdvīpa', 'जम्बूद्वीप', '赡部洲', 'jaina-philosophy', '佛典古译沿用（玫瑰苹果树洲；中洲）'),
    ('loka', 'लोक', '世界', 'jaina-philosophy', '耆那宇宙论（与 aloka 非世界对举）'),
    ('aloka', 'अलोक', '非世界', 'jaina-philosophy', '耆那宇宙论（世界外虚空）'),
    ('pradeśa', 'प्रदेश', '空间点', 'jaina-philosophy', '耆那宇宙论义译（不可分空间单位）'),
    ('skandha', 'स्कन्ध', '聚（物质聚）', 'jaina-philosophy', '耆那物质论义译；与佛教“蕴”分列'),
    ('samaya', 'समय', '刹那（相对时间）', 'jaina-philosophy', '耆那时间论（与 kāla 绝对时间对举）'),
    ('tiryañc', 'तिर्यञ्च', '傍生', 'jaina-philosophy', '印度宗教通行（与“动物”义近而含植物、元素生）'),
    ('manas', 'मनस्', '意', 'jaina-philosophy', '印度哲学通行（第六 sense 说）'),
    ('adhyavasāna', 'अध्यवसान', '执取', 'jaina-philosophy', '昆达昆达语境义译（意识的决取）'),
    ('bhāva', 'भाव', '情状', 'jaina-philosophy', '耆那教义译（心的状态）'),
    ('prakṛti', 'प्रकृति', '自性（prakṛti）', 'jaina-philosophy', '数论通行；与既有 puruṣa 神我 对举'),
    ('puruṣa', 'पुरुष', '神我', 'jaina-philosophy', '数论通行'),
    ('ātman', 'आत्मन्', '阿特曼（自我）', 'jaina-philosophy', '印度哲学通行；耆那语境同 jīva'),
    ('kaṣāya', 'कषाय', '烦恼', 'jaina-philosophy', '耆那业论通行（情欲之胶）'),
    ('yoga', 'योग', '瑜伽', 'jaina-philosophy', '通行（本文指修习）'),
    ('guṇasthāna', 'गुणस्थान', '阶位', 'jaina-philosophy', '耆那教通行（十四阶位）'),
    ('debating hall', '—', '论议堂', 'jaina-philosophy', '义译（印度辩论场）'),
    ('mati-jñāna', 'मतिज्ञान', '意觉知', 'jaina-philosophy', '耆那五种智之一，本库自拟'),
    ('śruta-jñāna', 'श्रुतज्ञान', '闻知', 'jaina-philosophy', '耆那五种智之一，本库自拟'),
    ('avadhi-jñāna', 'अवधिज्ञान', '有限知', 'jaina-philosophy', '耆那五种智之一（有限直接知），本库自拟'),
    ('manaḥparyaya-jñāna', 'मनःपर्ययज्ञान', '他心智', 'jaina-philosophy', '耆那五种智之一，本库自拟'),
    ('prameya', 'प्रमेय', '所量', 'jaina-philosophy', '因明通行'),
    ('vastu', 'वस्तु', '实（事物）', 'jaina-philosophy', '耆那实在论义译（多面之实）'),
    ('bhedābheda', 'भेदाभेद', '同异（不一不异）', 'jaina-philosophy', '吠檀多与耆那比较研究通行'),
    ('anyathānupapatti', 'अन्यथानुपपत्ति', '不可他存', 'jaina-philosophy', '耆那逻辑义译（非如此不可）'),
    ('sāgaropama', 'सागरोपम', '海劫', 'jaina-philosophy', '耆那宇宙论通行（海洋计年单位）'),
]

BOOKS = [
    ('Tattvārthasūtra (Umāsvāmin)', '—', '《论存在者》', 'jaina-philosophy',
     '既有作者行已立形（Umāsvāmin 行）；亦作《谛义经》；SEP 对题 Treatise on What There Is；简称 TS'),
    ('Tattvārthasūtrabhāṣya (Umāsvāti)', '—', '《论存在者疏》', 'jaina-philosophy', '随 Tattvārthasūtra；简称 TSBh'),
    ('Sarvārthasiddhi (Pūjyapāda)', '—', '《一切义成就》', 'jaina-philosophy', '既有作者行已立形（Pūjyapāda 行）；简称 SAS'),
    ('Samayasāra (Kundakunda)', '—', '《自我之精髓》', 'jaina-philosophy', '既有作者行已立形（Kundakunda 行）；简称 SSā'),
    ('Gommaṭasāra (Nemicandra)', '—', '《大雄教法之精髓》', 'jaina-philosophy', '既有作者行已立形（Nemicandra 行）；简称 GS'),
    ('Yogaśāstra (Hemacandra)', '—', '《瑜伽论》', 'jaina-philosophy', '既有作者行已立形（Hemacandra 行）；简称 YŚ'),
    ('Nyāyāvatāra (Siddhasena)', '—', '《逻辑导论》', 'jaina-philosophy', '既有作者行已立形（Siddhasena Mahāmati 行）；简称 NA'),
    ('Nyāyāvatāravivṛtti (Siddharṣigaṇi)', '—', '《逻辑导论注》', 'jaina-philosophy', '简称 NAv'),
    ('Āptamīmāṃsā (Samantabhadra)', '—', '《可信者探求》', 'jaina-philosophy', '简称 ĀMī；SEP 对题 Investigation on Authority'),
    ('Ratnakaraṇḍaśrāvakācāra (Samantabhadra)', '—', '《居士行仪宝箧》', 'jaina-philosophy', '简称 RKŚĀ'),
    ('Ācārāṅgasūtra', '—', '《威仪经》', 'jaina-philosophy', '简称 ĀS；SEP 对题 Canonical Text on Behavior'),
    ('Uttarādhyayana', '—', '《后分经》', 'jaina-philosophy', '简称 Utt.；SEP 对题 Later Chapters'),
    ('Sthānāṅgasūtra', '—', '《支分经》', 'jaina-philosophy', '简称 Ṭhāṇ.；SEP 对题 Canonical text on possibilities'),
    ('Bhagavatīsūtra', 'Vyākhyāprajñaptisūtra', '《世尊经》', 'jaina-philosophy', '简称 Viy.；SEP 对题 Venerable Exposition of teaching'),
    ('Jambūdvīpasaṃgrahaṇī (Haribhadra)', '—', '《赡部洲集》', 'jaina-philosophy', '简称 JDS；SEP 对题 Compendium of Middle Earth'),
    ('Anekāntajayapatākā (Haribhadra)', '—', '《多面性论胜幢》', 'jaina-philosophy', '简称 AJP；SEP 对题 Victory banner of the theory of non-one-sidedness'),
    ('Rājavārttika (Akalaṅka)', '—', '《王释》', 'jaina-philosophy', '简称 RV；SEP 对题 Royal Commentary'),
    ('Satyaśāsanaparīkṣā (Vidyānandin)', '—', '《正教探求》', 'jaina-philosophy', '简称 SŚP；既有作者行已立形'),
    ('Pramāṇanayatattvālokālaṃkāra (Vādi Devasūri)', '—', '《量·视角·谛光明庄严》', 'jaina-philosophy', '简称 PNT'),
    ('Prameyakāmalamārtaṇḍa (Prabhācandra)', '—', '《所量莲花日》', 'jaina-philosophy', '简称 PKM'),
    ('Jainatarkabhāṣā (Yaśovijaya)', '—', '《耆那逻辑手册》', 'jaina-philosophy', '简称 JTBh；既有作者行已立形'),
    ('Nyāyasūtra (Gautama)', '—', '《逻辑经》', 'jaina-philosophy', '既有行（Nyāya-sūtra）；简称 NS'),
    ('Nyāyasūtrabhāṣya (Vātsyāyana)', '—', '《逻辑经疏》', 'jaina-philosophy', '简称 NSBh'),
]

PERSONS = [
    ('Gautama (Indrabhūti)', 'Indrabhūti Gautama', '因陀罗菩提·乔答摩', '古印度（摩揭陀）／耆那教', '—', 'jaina-philosophy',
     '梵音自拟（大雄首徒；与 Gautama（正理）乔答摩分立）'),
    ('Prabhācandra', '—', '波罗婆旃陀罗', '古印度／耆那教', '980–1065', 'jaina-philosophy',
     '梵音自拟（《所量莲花日》作者）；生卒据 SEP 原文括注'),
    ('Siddharṣigaṇi', '—', '悉达湿迦尼', '古印度／耆那教', '约 900', 'jaina-philosophy',
     '梵音自拟（《逻辑导论注》作者）；年代据 SEP 原文括注'),
    ('Vādi Devasūri', '—', '瓦迪·提婆苏利', '古印度／耆那教', '1143', 'jaina-philosophy',
     '梵音自拟（《量·视角·谛光明庄严》作者）；年代据 SEP 原文括注'),
    ('Makkhali Gośāla', 'Makkhali Gosāla', '末伽梨·拘舍罗', '古印度（摩揭陀）／邪命外道', '—', 'jaina-philosophy',
     '佛典古译沿用（Ājīvika 派领袖）'),
]

tp = 'shu-yu-biao.md'
tl = io.open(tp, encoding='utf-8', newline='').read().split('\n')
for k, o, z, f, b in TERMS:
    add_term(tl, k, o, z, f, b)
for k, o, z, f, b in BOOKS:
    add_term(tl, k, o, z, f, b)
io.open(tp, 'w', encoding='utf-8', newline='\n').write('\n'.join(tl))

rp = 'ren-ming-biao.md'
rl = io.open(rp, encoding='utf-8', newline='').read().split('\n')
for o, a, z, r, lf, f, b in PERSONS:
    add_person(rl, o, a, z, r, lf, f, b)
io.open(rp, 'w', encoding='utf-8', newline='\n').write('\n'.join(rl))
print('DONE')

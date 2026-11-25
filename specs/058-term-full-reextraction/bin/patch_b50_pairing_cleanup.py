# -*- coding: utf-8 -*-
"""批 50：18 行审定引用按配对判据写实（ADR-0088 机检首扫的清账，2026-11-26）。

机检首扫出 21 行；其中 3 行（collective responsibility、imperfect information、unitary）
行内已写明审定收某复合词，判据补「收“／有“」后自动放行。余 18 行逐条按命中记录写实：
审定形、英文、分册、编号；四类关系如实注明（异拼／异序／复数／省略），两行改库别
（hypothetico-deductive 实为两岸库；transcendence 的审定「超越」是体育义项），
两行改源（tathāgatagarbha、vijñāna 实为中华思想文化术语传播工程非审定库）。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'

PATCH = {
    'analytical hierarchy': (
        '审定名词库（termonline-all，凭证 2026-11-23）',
        '审定作“解析分层”（analytic hierarchy，数学名词 02.0252；analytical 为异拼，2026-11-26 配对复核）',
    ),
    'argumentation': (
        '审定名词库（termonline-all·物理学·通类·物理，2026-11-18 JWT 直连凭证）；撞形改定 2026-11-21：论辩理论通行；论证归 Argument',
        '审定作“论证”（argumentation，物理学名词 01.0133；2026-11-26 界面精确匹配复核在案）；'
        '撞形改定 2026-11-21：论辩理论通行，与本行分域；论证归 Argument',
    ),
    'Chan Buddhism': (
        '审定名词库（termonline-all·中国古代史·隋唐五代·宗教，2026-10-31 浏览器通道凭证）',
        '审定作“禅宗”（Chan Zong;Zen Buddhism，中国古代史名词 5.246；2026-11-26 配对复核）',
    ),
    'completeness (space)': (
        '审定名词库（物理学名词 06.0500，相对论·量子理论；与逻辑“完全性”分立）',
        '审定作“完备性”（completeness，物理学名词 06.0500，相对论·量子理论；与逻辑“完全性”分立；'
        '键括注 (space) 为语境标记）',
    ),
    'disease burden': (
        '审定名词库（termonline-all，凭证 2026-11-23）',
        '审定作“疾病负担”（burden of disease, burden of illness，卫生经济学名词 12.2.1；'
        '英文侧同义异序，2026-11-26 配对复核）',
    ),
    'how-possibly explanations': (
        '审定名词库（termonline-all，凭证 2026-11-24）',
        '审定作“如何可能说明”（how-possible explanation，自然辩证法名词 03.431；本行复数形）',
    ),
    'hypothetico-deductive': (
        'FLAG 裁定 2026-11-21：审定名词库“假设─演绎”，维持（维持现译）',
        'FLAG 裁定 2026-11-21：海峡两岸名词对照库作“假设─演绎”（hypothetico-deductive；'
        '非审定公布库），维持（维持现译）',
    ),
    'iconic signs': (
        '审定名词库（termonline-all，凭证 2026-11-23）',
        '审定作“像似符号”（icon，新闻学与传播学名词 6.048；本行复数形）',
    ),
    'legal facts': (
        '审定名词库（termonline-all，凭证 2026-11-23）',
        '审定作“法律事实”（legal matter, juristic fact，管理科学技术名词 09.0567；英文侧同义异形）',
    ),
    'no-classes theory': (
        '审定名词库（termonline-all·自然辩证法，凭证 2026-11-23）',
        '审定作“无类理论”（no-class theory，自然辩证法名词 03.301；连字符与单复数异形）',
    ),
    'prenex form': (
        '审定名词库（termonline-all，凭证 2026-11-23）',
        '审定作“前束范式”（prenex normal form，数学名词 02.0063；本行省略 normal form）',
    ),
    'problem of induction': (
        '审定名词库（termonline-all，凭证 2026-11-23）',
        '审定作“归纳问题”（inductive problem，自然辩证法名词 03.083）',
    ),
    'rewrite rules': (
        '审定名词库（termonline-all，凭证 2026-11-23）',
        '审定作“重写规则”（rewriting rule，自动化名词 05.019；本行复数形）',
    ),
    'selection function': (
        '审定名词库（termonline-all·天文学·星系和宇宙学，2026-11-18 JWT 直连凭证）；撞形改定 2026-11-21：与选择函数（选择公理）分词',
        '审定作“选择函数”（selection function，天文学名词 07.296；2026-11-26 界面精确匹配复核在案）；'
        '撞形改定 2026-11-21：与本行“选取函数”分词，选择函数（选择公理）另键',
    ),
    'tathāgatagarbha': (
        '审定名词库（termonline-all·哲学，2026-10-31 浏览器通道凭证）',
        '中华思想文化术语传播工程作“如来藏”（Tathāgatagarbha / Womb of the Tathāgata；'
        '非审定公布库，2026-11-26 配对复核）',
    ),
    'token(令牌环语境)': (
        '审定名词（计算机科学技术名词）；凭证 2026-11-07',
        '海峡两岸信息科学技术名词作“令牌（＝权标）”（英文对照空缺；非审定公布库，2026-11-26 配对复核）；'
        '凭证 2026-11-07',
    ),
    'transcendence': (
        '审定名词库（termonline-all·心理学，2026-11-18 JWT 直连凭证）',
        '审定“超越”对应 overtaking（奥运体育项目名词），非哲学义；审定库无 transcendence 对口'
        '（2026-11-26 配对复核）',
    ),
    'vijñāna': (
        '审定名词库（termonline-all·哲学，2026-10-31 浏览器通道凭证）',
        '中华思想文化术语传播工程作“识”（Vijñāna / Consciousness；非审定公布库，2026-11-26 配对复核）',
    ),
}


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8:
                key = cells[1].strip()
                if key in PATCH:
                    old, new = PATCH[key]
                    if old not in cells[5]:
                        raise SystemExit('旧依据不符，中止：%s\n 实际：%s' % (key, cells[5].strip()))
                    cells[5] = cells[5].replace(old, new)
                    cells[6] = ' %s ' % DATE
                    line = '|'.join(cells)
                    done.add(key)
        out.append(line)
    missing = set(PATCH) - done
    if missing:
        raise SystemExit('未找到行：%s' % missing)
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 %d 行：%s' % (len(done), '、'.join(sorted(done))))


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""批 53：43 行“审定库无直接收录／无直接命中”全部界面精确匹配复核（2026-11-26）。

缘起：`complex conjugate` 一行原写“审定库无直接命中”，但物理学名词确有“复共轭”，
说明该族存在假阴性。43 行逐条走术语在线界面（精确匹配；译法形与各行亦作形全查），
结果三类：

  A 直配（负证不成立，改写为审定记录）：complex conjugate、efficient cause、
    hermeneutics、linear operator、mental processes、phronêsis、physical quantity、
    social justice。
  B 形近不采（审定有汉字同形但英文或义域不同，写明分册与不采理由）：Bildung、
    conscious experience、dimension、Encyclopédie、epistêmê、eudaimonia、
    Gödel number、moral worth、svabhāva、technê、tian。
  C 确认零条（原负证加复核戳，不删历史）：其余 24 行。

另：`norm` 一项译法由“模”改“范数”——审定库 norm 对“范数”（数学名词、物理学名词），
“模”在审定库对 mode/module/modulus；本表 t-范数、三角范数等行亦用“范数”，归一口径。

所有改动按「键＋旧串严格匹配」执行，旧串找不到即中止（防静默错改）。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'
STAMP29 = '（凭证 2026-10-29）'
STAMP30 = '（凭证 2026-10-30）'

# 键 -> (旧串, 新串)；键在表内唯一，旧串必须原样出现
REWRITE = {
    'complex conjugate': (
        '学界惯例（复变函数通行；审定库无直接命中）；凭证 2026-11-11',
        '审定作“复共轭”（complex conjugate，物理学名词；2026-11-26 界面精确匹配复核）；'
        '复变函数通行'),
    'efficient cause': (
        '学界惯例（亚氏四因通行译名）；审定库无直接收录（凭证 2026-10-29）；'
        '佐证审定库同系列“质料因/形式因”（凭证 2026-10-29）',
        '审定作“动力因”（英文列作 effect cause，自然辩证法名词 2024；2026-11-26 界面精确匹配复核）；'
        '亚氏四因通行译名；审定同系列另有“质料因/形式因”'),
    'hermeneutics': (
        '权威译本通行译法（洪汉鼎《真理与方法》）；审定库无直接收录（凭证 2026-11-01）',
        '权威译本通行译法（洪汉鼎《真理与方法》）；审定作“诠释学”（hermeneutics，自然辩证法名词）；'
        '海峡两岸名词对照库（地理学）作“解释学”（2026-11-26 界面精确匹配复核）'),
    'linear operator': (
        '学界惯例（量子力学教科书通行；审定库无直接命中）；凭证 2026-11-11',
        '审定作“线性算符”（linear operator，物理学名词；2026-11-26 界面精确匹配复核）；'
        '量子力学教科书通行'),
    'mental processes': (
        '学界惯例（心灵哲学通行）；审定库无直接收录（凭证 2026-10-30）',
        '审定作“心理过程”（mental process，心理学名词、行为医学名词各 1 条；'
        '2026-11-26 界面精确匹配复核）；心灵哲学通行'),
    'phronêsis': (
        '学界惯例（亚里士多德译本通行）；审定库无直接收录（凭证 2026-10-30）；',
        '审定作“实践智慧”（phronesis，自然辩证法名词；2026-11-26 界面精确匹配复核）；'
        '亚里士多德译本通行；'),
    'physical quantity': (
        '学界惯例（物理学通行；审定库无直接命中）；凭证 2026-11-11',
        '审定作“物理量”（physical quantity，物理学名词；2026-11-26 界面精确匹配复核）；'
        '物理学通行'),
    'social justice': (
        '学界惯例（政治哲学/罗尔斯译本通行）；审定库无直接收录（凭证 2026-10-29）；'
        '审定库“社会公正”为地理学域不采（凭证 2026-10-29）',
        '审定作“社会正义”（social justice，社会学名词、社会医学名词各 1 条；'
        '2026-11-26 界面精确匹配复核）；政治哲学/罗尔斯译本通行'),
}

# B 类：汉字同形、英文或义域不同，写明不采理由
NEAR = {
    'Bildung': (
        '学界惯例（伽达默尔《真理与方法》通行）；审定库无直接收录（凭证 2026-10-30）',
        '学界惯例（伽达默尔《真理与方法》通行）；审定“教化”（教育学名词 2013，'
        '中国教育史：儒家政教主张）系汉字同形异概念，不采（2026-11-26 界面复核）'),
    'conscious experience': (
        '学界惯例（心灵哲学通行）；审定库无直接收录（凭证 2026-10-29）；'
        '审定库命中医学域“意识性体验”不采（凭证 2026-10-29）',
        '学界惯例（心灵哲学通行）；审定“意识性体验”（英文列作 conscious experience，'
        '睡眠医学名词 2022）中文形异、义域为睡眠医学，不采（2026-11-26 界面复核）'),
    'dimension': (
        '学界惯例（线性代数通行；审定库无直接命中）；凭证 2026-11-11',
        '学界惯例（线性代数通行）；审定“维度”（dimension，核医学名词）为同一英文的异构形，'
        '数学语境通行“维数”未见收录（2026-11-26 界面精确匹配复核）；凭证 2026-11-11'),
    'Encyclopédie': (
        '学界惯例（启蒙哲学译名）；审定库无直接收录（凭证 2026-10-30）',
        '学界惯例（启蒙哲学译名）；审定“百科全书”（encyclopedia，编辑与出版学、'
        '图书馆·情报与文献学、语言学名词共 3 条）为书类通名，非本条专名（2026-11-26 界面复核）'),
    'epistêmê': (
        '学界惯例（希腊哲学术语）；审定库无直接收录（凭证 2026-10-30）；',
        '学界惯例（希腊哲学术语）；审定“知识”（knowledge，图书馆·情报与文献学、'
        '计算机科学技术、管理科学技术名词等 4 条）佐证译形，英文对 knowledge（2026-11-26 界面复核）；'),
    'eudaimonia': (
        '学界惯例（亚里士多德译本通行）；审定库无直接收录（凭证 2026-10-30）；'
        '审定库精确查无（凭证 2026-10-30）；',
        '学界惯例（亚里士多德译本通行）；审定“幸福”（happiness，医学伦理学名词）佐证译形，'
        '英文对 happiness 非 eudaimonia（2026-11-26 界面复核）；'),
    'Gödel number': (
        '学界惯例（数理逻辑通行）；审定库无直接收录（凭证 2026-10-30）',
        '学界惯例（数理逻辑通行）；审定“哥德尔配数”（Gödel numbering，计算机科学技术名词 2018）'
        '为编码方式，与本条“数”系同一构念的相邻形（2026-11-26 界面复核）'),
    'moral worth': (
        '学界惯例（伦理学/康德译本通行）；审定库无直接收录（凭证 2026-10-30）',
        '学界惯例（伦理学/康德译本通行）；审定“道德价值”（moral value，医学伦理学名词）'
        '英文对 moral value，非 moral worth（2026-11-26 界面复核）'),
    'svabhāva': (
        '学界惯例（佛典译语）；审定库无直接收录（凭证 2026-10-30）；审定库精确查无（凭证 2026-10-30）',
        '学界惯例（佛典译语）；审定“自性”（prakrti，自然辩证法名词）系数论概念，'
        '与佛教 svabhāva 非同概念，不采（2026-11-26 界面复核）'),
    'technê': (
        '学界惯例（希腊哲学术语）；审定库无直接收录（凭证 2026-10-30）；',
        '学界惯例（希腊哲学术语）；审定“技艺”（technique，自然辩证法名词）英文对 technique，'
        '与 τέχνη 义近（2026-11-26 界面复核）；'),
    'tian': (
        '学界惯例（拼音与汉字对应）；审定库无直接收录（凭证 2026-10-30）',
        '学界惯例（拼音与汉字对应）；其他术语库“中华思想文化术语传播工程”作“天”'
        '（Tian (Heaven)，哲学；非审定公布库，2026-11-26 界面复核）'),
    'norm': (
        '学界惯例（矢量长度；审定库无直接命中）；凭证 2026-11-11',
        '审定作“范数”（norm，数学名词、物理学名词各 1 条；2026-11-26 界面精确匹配复核）；'
        '“模”在审定库对 mode/module/modulus，非本义'),
}

# C 类：确认零条，加复核戳（保留原负证与日期）
ZERO = {
    'categorical imperative': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：'
                                          '定言命令、绝对命令均 0 条）'),
    'Cauchy sequence': ('；凭证 2026-11-11', '；凭证 2026-11-11；'
                        '2026-11-26 界面精确匹配复核：柯西序列 0 条'),
    'comprehension principle': (
        '审定库无直接收录（凭证 2026-10-30）',
        '审定“概括公理”（comprehension axiom，数学名词）已列 comprehension axiom 行；'
        '“概括原则”本身 0 条（2026-11-26 界面精确匹配复核）'),
    'difference principle': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：'
                                      '差别原则 0 条）'),
    'epistemic closure': (
        '审定库无直接命中（凭证 2026-10-31）',
        '审定库无直接命中（凭证 2026-10-31；2026-11-26 界面精确匹配复核：认知闭合、认知封闭均 0 条）'),
    'epistemic injustice': (STAMP30, '（凭证 2026-10-30；2026-11-26 界面精确匹配复核：'
                                     '认知不义、认知不公正均 0 条）'),
    'eternal truths': (STAMP30, '（凭证 2026-10-30；2026-11-26 界面精确匹配复核：永恒真理 0 条）'),
    'formal logic': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：形式逻辑 0 条）'),
    'human action': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：人类行动 0 条）'),
    'infinite regress': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：'
                                  '无穷倒退、无限倒退、无限回溯均 0 条）'),
    'innate knowledge': (STAMP30, '（凭证 2026-10-30；2026-11-26 界面精确匹配复核：'
                                  '天赋知识、先天知识均 0 条）'),
    'logical constants': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：逻辑常项 0 条）'),
    'mental events': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：心理事件 0 条）'),
    'moral obligation': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：道德义务 0 条）'),
    'natural deduction': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：自然演绎 0 条）'),
    'nous': (STAMP30, '（凭证 2026-10-30；2026-11-26 界面精确匹配复核：努斯、理智均 0 条）'),
    'physical states': (STAMP30, '（凭证 2026-10-30；2026-11-26 界面精确匹配复核：物理状态 0 条）'),
    'rational beings': (STAMP30, '（凭证 2026-10-30；2026-11-26 界面精确匹配复核：理性存在者 0 条）'),
    'religious belief': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：宗教信念 0 条）'),
    'scientific practice': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：科学实践 0 条）'),
    'ultimate reality': (STAMP29, '（凭证 2026-10-29；2026-11-26 界面精确匹配复核：终极实在 0 条）'),
    'virtuous person': (STAMP30, '（凭证 2026-10-30；2026-11-26 界面精确匹配复核：'
                                 '有德之人、有德者、德性之人均 0 条）'),
    'dharma / dharmas': (
        '学界惯例（佛典译语）；审定库无直接收录（凭证 2026-10-30）；',
        '学界惯例（佛典译语）；审定库无佛学“法”条目（精确匹配命中的“法”为档案学 fa、'
        '“法律”为放射医学；“达摩” 0 条；2026-11-26 界面复核）；'),
}

# 译法改写（仅 norm）：审定 norm＝范数，“模”对 mode/module/modulus
TRANS = {'norm': ('模', '范数（亦作“模”）')}


def apply_row(cells, key):
    """返回 (cells, 改动说明) 或 None（无改动）。"""
    changed = []
    if key in TRANS:
        old, new = TRANS[key]
        if cells[3].strip() != old:
            raise SystemExit('%s 译法非预期：%r' % (key, cells[3]))
        cells[3] = ' %s ' % new
        changed.append('译法')
    for table, tag in ((REWRITE, 'A'), (NEAR, 'B'), (ZERO, 'C')):
        if key in table:
            old, new = table[key]
            if old not in cells[5]:
                raise SystemExit('%s 旧串未找到（%s）：%r' % (key, tag, old))
            cells[5] = cells[5].replace(old, new, 1)
            changed.append(tag)
    if not changed:
        return None
    cells[6] = ' %s ' % DATE
    return changed


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = {}, []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8:
                key = cells[1].strip()
                got = apply_row(cells, key)
                if got:
                    done[key] = ''.join(got)
                    line = '|'.join(cells)
        out.append(line)
    expect = set(REWRITE) | set(NEAR) | set(ZERO)
    missing = expect - set(done)
    if missing:
        raise SystemExit('漏改 %d 行：%s' % (len(missing), '、'.join(sorted(missing))))
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 %d 行（A %d／B %d／C %d，norm 另改译法）' % (
        len(done), len(REWRITE), len(NEAR), len(ZERO)))


if __name__ == '__main__':
    main()

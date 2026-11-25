# -*- coding: utf-8 -*-
"""批 57：“审定库无对口命中”族界面复核（2026-11-26，24 行）。

缘起：批 55 之后继续清负证。886 行“无对口命中”先用本地索引做高召回预筛（审定库里只要
存在同中文形条目就标出），25 行可疑；逐条走界面精确匹配，22 行需改（另 2 行已于
2026-11-25 缓存重放补正，1 行 ε 演算为扫描假阳性）。

判定要点：索引条目可能是模糊邻居（`兼爱` 在缓存里挂“社会学名词”，界面实为中华思想文化
术语传播工程），故一律以界面为准。

  直配 14：丘奇论题、休谟原则、马赫原理（已补正）、广延量、思想史、语言模型、医学伦理学、
    道德实践、自然美、非经典逻辑、零假设、研究伦理、斯科伦悖论、时间贴现、芝诺悖论。
  形同义异／语义近 7：自欺（self-deception）、集体意识（仅海峡两岸）、描述函数（控制论）、
    兼爱（其他术语库）、心理词典（mental lexicon）、操作分析（operating analysis）、
    器官买卖（organ trafficking）、超越自我（surmount oneself）。

改法：原负证保留，后接“2026-11-26 界面复核改判”。
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'

FIX = {
    'bad faith': '审定“自欺”（self-deception，心理学名词）；英文义为自我欺骗，与本行萨特'
                 '“自欺”形同而义域不同，作佐证',
    "Church's thesis": '审定作“丘奇论题”（Church thesis，数学名词）',
    'collective consciousness': '仅海峡两岸名词对照库作“集体意识”'
                                '（collective consciouness，地理学名词），审定公布库无',
    'descriptive functions': '审定“描述函数”（describing function，电气工程、电子学、自动化名词）'
                             '系控制论义，与描述函项非同概念，不采',
    'extensive magnitudes': '审定作“广延量”（extensive quantity，物理学名词）',
    "Hume's Principle": '审定作“休谟原则”（Hume’s principle，自然辩证法名词）',
    'impartial care': '其他术语库“中华思想文化术语传播工程”作“兼爱”'
                      '（Universal Love，哲学），审定公布库无',
    'intellectual history': '审定作“思想史”（intellectual history，社会学名词）',
    'language model': '审定作“语言模型”（language model，计算机科学技术名词；'
                      '“语言学名词”作 linguistic model）',
    'medical ethics': '审定作“医学伦理学”（medical ethics，自然辩证法名词）',
    'mental dictionary': '审定“心理词典”（mental lexicon，心理学名词）；英文对 mental lexicon，'
                         '本行 mental dictionary 义近，主译保留',
    'moral practice': '审定作“道德实践”（moral practice，教育学名词）',
    'natural beauty': '审定作“自然美”（beauty of nature，自然辩证法名词）',
    'nonclassical logics / non-classical logics':
        '审定作“非经典逻辑”（non-classical logic，计算机科学技术名词）',
    'null hypotheses': '审定作“零假设”（null hypothesis，经济学、化学工程、肠外肠内营养学等名词共 6 条）',
    'operational analysis': '审定“操作分析”（operating analysis，教育学名词）系 operating analysis 义，'
                            '非同概念，不采',
    'organ sale': '审定“器官买卖”（organ trafficking，医学伦理学名词）；英文对 organ trafficking'
                  '（贩运），与本行买卖义有别，主译保留',
    'research ethics': '审定作“研究伦理”（research ethics，自然辩证法名词）',
    "Skolem's Paradox": '审定作“斯科伦悖论”（Skolem’s paradox，自然辩证法名词）',
    'time discounting': '审定作“时间贴现”（time discount，食品卫生学名词）',
    'transcendent self': '审定“超越自我”（surmount oneself，资源科学技术名词），非同概念，不采',
    'Zeno’s paradox': '审定作“芝诺悖论”（Zeno’s paradox，自然辩证法名词）',
}

CLAIM = re.compile(r'审定库(?:镜像)?无对口命中，(\d{4}-\d{2}-\d{2})')


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8:
                key = cells[1].strip()
                if key in FIX:
                    new = CLAIM.sub(
                        lambda m: '原记无对口命中（%s，缓存通道），%s 界面精确匹配复核改判：%s'
                                  % (m.group(1), DATE, FIX[key]), cells[5], count=1)
                    if new == cells[5]:
                        raise SystemExit('%s 未替换，检查措辞' % key)
                    cells[5] = new
                    cells[6] = ' %s ' % DATE
                    done.add(key)
                    line = '|'.join(cells)
        out.append(line)
    missing = set(FIX) - done
    if missing:
        raise SystemExit('漏改：%s' % '、'.join(sorted(missing)))
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改判 %d 行' % len(done))


if __name__ == '__main__':
    main()

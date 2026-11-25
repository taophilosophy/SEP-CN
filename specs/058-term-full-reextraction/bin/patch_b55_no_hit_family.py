# -*- coding: utf-8 -*-
"""批 55：「审定库无相关命中」族 172 行界面精确匹配复核（2026-11-26）。

缘起：批 53 复核“无直接收录”族时发现负证有假阴性；本族更早（2026-10-31／11-13 缓存
通道）留下的负证同病。172 行逐条走术语在线界面精确匹配（书名类 35 行不查——审定库不收
书题），概念类 137 形结果：

  直配 9：arché→“本原”（arche，自然辩证法名词）、Bedeutung→“意义”（meaning）、
    kinêsis→“运动”（motion）、neo-Kantianism→“新康德主义”（NeoKantianism，马克思主义）、
    phenomenology→“现象学”（phenomenology，心理学名词）、pluralist theories→“多元论”
    （pluralism，地理学名词）、Sittlichkeit→“伦理”（ethics，阿尔茨海默病名词）、
    social facts→“社会事实”（social fact，社会学／民族学与文化学名词）、
    Vorstellung→“表象”（representation，物理学名词 2019；mental image，心理学／行为医学）。
  形近／库别 7：aisthêsis（仅海峡两岸“感知”）、deflationary（仅海峡两岸“紧缩”）、
    aretê／Pure Land／saṃsāra（其他术语库“德性／净土／轮回”）、pure reason（征求意见库
    “纯粹理性”，预公布）、identity relation（审定“等同关系”以“同一关系”为又称，
    系索引语义关系义，不采）。
  确认 0 条：其余 156 行，原负证加界面复核戳，不删历史。

旧负证原样保留在括号里，改判写在后面（“不删历史”口径同批 52／53）。
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'
CLAIM = re.compile(r'审定库无相关命中（([^）]*)）')

# 键 -> 改判说明（写在原凭证之后）
FIX = {
    'arché': '审定作“本原”（arche，自然辩证法名词）',
    'aisthêsis': '仅海峡两岸名词对照库作“感知”（perception），审定公布库无',
    'aretê': '其他术语库“中华思想文化术语传播工程”作“德性”'
             '（Virtuous Nature / Morals as Human Nature），审定公布库无',
    'Bedeutung': '审定作“意义”（meaning，新闻学与传播学名词、语言学名词）',
    'deflationary': '仅海峡两岸名词对照库作“紧缩”（信息科学技术），审定公布库无',
    'identity relation': '审定“等同关系”（equivalence relation，图书馆·情报与文献学名词 2019）'
                         '以“同一关系”为又称，系索引词语义关系义，非逻辑同一性义，不采',
    'kinêsis': '审定作“运动”（motion，自然辩证法名词）',
    'neo-Kantianism': '审定作“新康德主义”（NeoKantianism，马克思主义）',
    'phenomenology': '审定作“现象学”（phenomenology，心理学名词）',
    'pluralist theories': '审定作“多元论”（pluralism，地理学名词）',
    'Pure Land': '其他术语库“中华思想文化术语传播工程”作“净土”'
                 '（Sukhāvatīvyūha / Pure Land），审定公布库无',
    'pure reason': '征求意见库·马克思主义作“纯粹理性”（又称“纯理性”，pure reason；'
                   '预公布未正式公布）',
    'saṃsāra': '其他术语库“中华思想文化术语传播工程”作“轮回”'
               '（Samsāra / Rebirth / Reincarnation），审定公布库无',
    'Sittlichkeit': '审定作“伦理”（ethics，阿尔茨海默病名词）',
    'social facts': '审定作“社会事实”（social fact，社会学名词、民族学与文化学名词）',
    'Vorstellung': '审定作“表象”（representation，物理学名词 2019，又称“表示”；'
                   'mental image，心理学名词、行为医学名词）',
}


def rewrite(key, basis):
    def sub(m):
        old = m.group(1)
        if key in FIX:
            return '审定库无相关命中（%s；2026-11-26 界面复核改判：%s）' % (old, FIX[key])
        return '审定库无相关命中（%s；2026-11-26 界面精确匹配复核：0 条）' % old
    return CLAIM.sub(sub, basis)


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    n, hits = 0, 0
    out = []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8 and '无相关命中' in cells[5]:
                key = cells[1].strip()
                new = rewrite(key, cells[5])
                if new == cells[5]:
                    raise SystemExit('%s 未替换，检查措辞' % key)
                hits += int(key in FIX)
                cells[5] = new
                cells[6] = ' %s ' % DATE
                line = '|'.join(cells)
                n += 1
        out.append(line)
    if n != 172:
        raise SystemExit('应改 172 行，实改 %d 行' % n)
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('复核戳 %d 行（其中改判 %d 行）' % (n, hits))


if __name__ == '__main__':
    main()

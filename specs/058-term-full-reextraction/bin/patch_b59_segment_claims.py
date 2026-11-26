# -*- coding: utf-8 -*-
"""批 59：分句判据掀出的 9 行写实（2026-11-26）。

按分句判“审定主张须引形”后，整行豁免掩掉的 8 行裸断言＋1 行混标暴露出来，逐条界面
精确匹配复核（2026-11-26）：

  直配 5：大弃赌论证（Dutch book arguments，自然辩证法名词 03.221）、平等主义
    （equalitarianism，教育学名词 08.267）、直觉主义逻辑（intuitionist logic，数学名词
    02.0123）、潜变量（社会学名词·数据分析 2025）。
  库别 3：缘起（Dependent Origination）、业（Karma）只见其他术语库“中华思想文化术语
    传播工程”；命题逻辑只见海峡两岸名词对照库（信息科学技术 2008）。
  形同异库 1：尽责性的“严谨性”只见海峡两岸名词对照库（conscientiousness，心理学名词），
    审定公布库无“尽责性”，原“审定/他量表形”表述改正。

另：transcendence 行“审定库无 transcendence 对口”句带空格，负证正则补
`无[^；，]{0,24}对口`。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'

FIX = {
    'conscientiousness': [
        ('“严谨性”为审定/他量表形',
         '“严谨性”仅见海峡两岸名词对照库（conscientiousness，心理学名词），审定公布库无'
         '“尽责性”（2026-11-26 界面复核；非审定公布库）'),
    ],
    'dependent origination': [
        ('审定名词库（termonline-all·哲学，2026-11-18 JWT 直连凭证）',
         '其他术语库“中华思想文化术语传播工程”作“缘起”（Dependent Origination，哲学；'
         '非审定公布库，2026-11-26 界面复核）；审定公布库无'),
    ],
    'Dutch Book Arguments': [
        ('审定名词库（termonline-all·自然辩证法·科学哲学·一般科学哲学·认识论，'
         '2026-11-18 JWT 直连凭证）',
         '审定作“大弃赌论证”（Dutch book arguments，自然辩证法名词 03.221；'
         '2026-11-26 界面精确匹配复核）'),
    ],
    'egalitarianism': [
        ('审定库复核一致（termonline-all 浏览器通道凭证 2026-10-29；2026-11-25 界面精确匹配复核在案）',
         '审定作“平等主义”（equalitarianism，教育学名词 08.267；英文为 equalitarianism 形；'
         '2026-11-26 界面精确匹配复核）'),
    ],
    'intuitionistic logic': [
        ('审定库复核一致（termonline-all 浏览器通道凭证 2026-10-29；2026-11-25 界面精确匹配复核在案）',
         '审定作“直觉主义逻辑”（intuitionist logic，数学名词 02.0123；海峡两岸信息科学技术名词'
         '另收 intuitionistic logic 形；2026-11-26 界面精确匹配复核）'),
    ],
    'karma': [
        ('审定名词库（termonline-all·哲学，2026-11-18 JWT 直连凭证）',
         '其他术语库“中华思想文化术语传播工程”作“业”（Karma，哲学；非审定公布库，'
         '2026-11-26 界面复核）；审定公布库无'),
    ],
    'propositional logic / propositional calculus': [
        ('审定名词库（海峡两岸信息科学技术名词·信息科学技术，2008；凭证 2026-11-22）',
         '海峡两岸名词对照库作“命题逻辑”（propositional logic，信息科学技术，2008；'
         '非审定公布库，2026-11-26 界面复核）；审定公布库无'),
    ],
    'latent variable': [
        ('审定名词库（社会学名词·数据分析，2025 作“潜变量”；海峡两岸心理学名词 2016 作'
         '“潜［在］变量”；2026-11-25 缓存重放补正）',
         '审定作“潜变量”（社会学名词·数据分析，2025）；海峡两岸名词对照库作“潜［在］变量”'
         '（心理学名词，2016；非审定公布库）（2026-11-26 界面复核）'),
    ],
}


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8 and cells[1].strip() in FIX:
                key = cells[1].strip()
                for old, new in FIX[key]:
                    if old not in cells[5]:
                        raise SystemExit('%s 旧串未找到：%r' % (key, old[:40]))
                    cells[5] = cells[5].replace(old, new, 1)
                cells[6] = ' %s ' % DATE
                done.add(key)
                line = '|'.join(cells)
        out.append(line)
    missing = set(FIX) - done
    if missing:
        raise SystemExit('漏改：%s' % '、'.join(sorted(missing)))
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 %d 行' % len(done))


if __name__ == '__main__':
    main()

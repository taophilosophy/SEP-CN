# -*- coding: utf-8 -*-
"""批 41：按界面“精确匹配”复核结果改正依据列（2026-11-25）。

只改“凭证与事实不符”的七行；译法一字不动。逐行严格比对旧依据，找不到即中止，
防止在共用工作区里误改他行。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-25'

PATCH = {
    'archimedean property': (
        '审定名词库数学通行译名；凭证 2026-11-11',
        '数学界通行译名；审定名词库无“阿基米德性质”条目（仅有阿基米德公理、阿基米德序域、阿基米德绝对值等，'
        '2026-11-25 界面精确匹配复核；旧记“审定名词库数学通行译名”系模糊匹配所得，已改正）',
    ),
    'canonically conjugate': (
        '审定名词库（物理学名词）；凭证 2026-11-09',
        '审定名词库物理学名词作“正则共轭变量”（canonical conjugate variable，02.0604）；本行为其名词化，'
        '审定库无独立“正则共轭”条目（2026-11-25 界面精确匹配复核；旧记系模糊匹配所得，已改正）',
    ),
    'knowing how': (
        '审定名词库（termonline-all，凭证 2026-11-23）；主形改定：abilities 条目作“知道如何”；'
        '原“技能知识”全库 0 处（2026-11-24 语料核对，凭证 works-batch33-2026-11-24.md）',
        '技能哲学通行译法（Ryle 谱系）；审定库无对口条目——英文精确匹配 0 条，中文“知道如何”亦未审定，'
        '缓存中“技能知识”各条无审定出处（2026-11-25 界面复核；旧记“审定名词库”系模糊匹配所得，已改正）；'
        '主形改定：abilities 条目作“知道如何”；原“技能知识”全库 0 处（2026-11-24 语料核对，凭证 works-batch33-2026-11-24.md）',
    ),
    'empiricist': (
        '审定名词库（termonline-all·心理学，2026-11-18 JWT 直连凭证）',
        '海峡两岸名词对照库（心理学，2016）作“经验主义者,经验论者”（台湾名“經驗主義者,經驗論者,實徵論者”）；'
        '审定公布名词库无对口条目（2026-11-25 界面精确匹配复核；旧记“审定名词库”已改正）',
    ),
    'samadhi': (
        '佛教汉语传统译名；审定名词库（海峡两岸心理学名词，2016）作“禅定”，佛教传统译名“三昧”优先，保留'
        '（凭证 termonline-b10-2026-11-24.tsv）',
        '佛教汉语传统译名；海峡两岸名词对照库（心理学，2016）作“禅定”，审定公布名词库无对口条目；'
        '佛教传统译名“三昧”优先，保留（凭证 termonline-b10-2026-11-24.tsv；2026-11-25 界面复核，旧记库名表述有误已改正）',
    ),
    'teleportation': (
        '审定名词库（termonline·物理学名词）；凭证 2026-11-09',
        '审定名词库“量子隐形传态”（quantum teleportation；自然辩证法名词·物理学哲学／光学名词／计算机科学技术名词，'
        '2026-11-25 界面精确匹配复核）；本行缩略作“隐形传态”，审定库无裸词条目',
    ),
    'fundamentalism': (
        '学界通行（宗教研究）；凭证 2026-11-11；审定名词库（社会学名词 3.9.1.15，2025）作“原教旨主义”，'
        '宗教学通行“基要主义”，保留并注（凭证 termonline-b5-2026-11-24.tsv）',
        '学界通行（宗教研究）；凭证 2026-11-11；名词库（社会学名词 3.9.1.15，2025）作“原教旨主义”，'
        '宗教学通行“基要主义”，保留并注；该条 2026-11-25 界面标注“尚未正式公布”并挂“发表意见”，引用按预公布处理'
        '（凭证 termonline-b5-2026-11-24.tsv）',
    ),
}


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done = set()
    out = []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8:
                key = cells[1].strip()
                if key in PATCH:
                    old, new = PATCH[key]
                    if cells[5].strip() != old:
                        raise SystemExit('旧依据不符，中止：%s\n  实际：%s' % (key, cells[5].strip()))
                    cells[5] = ' ' + new + ' '
                    cells[6] = ' ' + DATE + ' '
                    line = '|'.join(cells)
                    done.add(key)
        out.append(line)
    missing = set(PATCH) - done
    if missing:
        raise SystemExit('未找到行：%s' % missing)
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('已改正 %d 行依据：%s' % (len(done), '、'.join(sorted(done))))


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""批 58：小族负证界面复核（2026-11-26，8 行）。

886 行“无对口”清完后继续核其余小族（查无／未见／未收／无查询件），45 行逐条走界面：
 直配 5：Russell’s Paradox→“罗素悖论”（自然辩证法名词）、Bell inequalities→“贝尔不等式”
   （物理学名词）、Lehrfreiheit→“教学自由”（freedom of teaching，教育学名词）、
   Lernfreiheit→“学习自由”（freedom of learning，教育学名词）、spacelike separation→
   “类空间隔”（spacelike interval，物理学名词）。
 形同义异／其他库 3：isonomia 的“平等”仅见其他术语库（传播工程 Equality）；kenon 的
   “空腔”是 cavity pocket（电力）／air containing space（结核病学）义；poroi 的“通道”
   为 alley way／passage／channel 等交通信道义。
 其余确认 0 条（贝尔定理、机械论、感官知觉、观察句、谓词字母、现在主义、确证理论、
   经典一阶逻辑、可数无穷、射影集合、同源同一、机构中立、超决定论、万有在神论、
   斯宾诺莎主义、毕达哥拉斯主义、苏格兰哲学、德国哲学、普遍教学权、大学大宪章、专权、
   论自然者、汇通、CHSH 不等式、权威主义人格、不可知觉的东西、学述传统），不另行改行。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'
OLD_CHACU = '审定库复核查无（termonline-all 浏览器通道 2026-10-29）'

FIX = {
    'Bell inequalities': (
        '审定库复核在案（同名噪声/辅助档差异，保留现译 2026-10-29）',
        '审定作“贝尔不等式”（Bell inequality，物理学名词；2026-11-26 界面精确匹配复核改判）'),
    'isonomia': (
        OLD_CHACU,
        OLD_CHACU[:-1] + '；2026-11-26 界面复核：审定公布库无，其他术语库'
        '“中华思想文化术语传播工程”作“平等”（Equality，历史））'),
    'kenon': (
        OLD_CHACU,
        OLD_CHACU[:-1] + '；2026-11-26 界面复核：审定“空腔”系 cavity pocket（电力名词）'
        '／air containing space（结核病学名词）义，非同概念，不采）'),
    'Lehrfreiheit': (
        OLD_CHACU,
        OLD_CHACU[:-1] + '；2026-11-26 界面复核改判：审定作“教学自由”'
        '（freedom of teaching，教育学名词））'),
    'Lernfreiheit': (
        OLD_CHACU,
        OLD_CHACU[:-1] + '；2026-11-26 界面复核改判：审定作“学习自由”'
        '（freedom of learning，教育学名词））'),
    'poroi': (
        OLD_CHACU,
        OLD_CHACU[:-1] + '；2026-11-26 界面复核：审定“通道”为 alley way／passage／channel '
        '等交通与信道义共 14 条，非同概念，不采）'),
    'Russell’s Paradox': (
        '审定库查无对应条目',
        '审定作“罗素悖论”（Russell’s paradox，自然辩证法名词；2026-11-26 界面精确匹配复核改判）'),
    'spacelike separation': (
        OLD_CHACU,
        OLD_CHACU[:-1] + '；2026-11-26 界面复核改判：审定作“类空间隔”'
        '（spacelike interval，物理学名词））'),
}


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8:
                key = cells[1].strip()
                if key in FIX:
                    old, new = FIX[key]
                    if old not in cells[5]:
                        raise SystemExit('%s 旧串未找到' % key)
                    cells[5] = cells[5].replace(old, new, 1)
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

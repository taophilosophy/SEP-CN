# -*- coding: utf-8 -*-
"""批 54：库名如实机检暴露的 23 行失实 + 6 行裸断言写实（2026-11-26）。

机检新增第三项检查（tools/term_pairing.audit_citation_libs）：凡行内写「审定…作“X”」，
就按 X 在索引里的实际库别核。结果 23 行失实，成因两类：

  1. 16 行同一句式——2026-11-18 JWT 直连批量查证时把 `termonline-all` 整站统称“审定名词库”，
     而命中的分册其实来自海峡两岸名词对照库（心理学／地理学／信息科学技术／植物学／
     经贸／航海／大气科学／化学工程）或中华思想文化术语传播工程（哲学／文艺）。
  2. 7 行措辞混标（agreeableness、organism、center of oscillation、lunar inequality 等）。

另 6 行只写了库名没写审定形（裸断言），按索引条目写实：accidental generalization、
action quantum、evolutionary game theory、free speech、Stoic、śūnyatā。

改法：库名换成实际库别，多余的“审定”二字去掉，补“非审定公布库”与索引复核日期；
不删历史凭证与日期。旧串严格匹配，找不到即中止。
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'

TW = '海峡两岸名词对照库'
OTHER = '其他术语库'

# 键 -> 实际库别（用于通用句式改写）
LIBFIX = {
    'abnormality': TW,
    'Anti-essentialism': TW,
    'Catholicism': TW,
    'conclusive evidence': TW,
    'intrinsic function': TW,
    'irregularity': TW,
    'language acquisition': TW,
    'mutual acceptance': TW,
    'negative identity': TW,
    'pluralistic ignorance': TW,
    'possibilist': TW,
    'recursion': TW,
    'social conventions': TW,
    'icchantika': OTHER,
    'introspection': OTHER,
    'junzi': OTHER,
    'kindness': OTHER,
    'moral cultivation': OTHER,
    'non-action': OTHER,
}

# 键 -> [(旧串, 新串)]；特殊措辞行与裸断言行
SPECIAL = {
    'agreeableness': [
        ('（2026-11-24 复核）审定库（海峡两岸心理学名词，2016）作“亲和性”，系对照库非审定公布库',
         '（2026-11-24 复核）%s（termonline-all·心理学名词，2016）作“亲和性”，非审定公布库' % TW),
    ],
    'organism': [
        ('2026-11-18 JWT 直连凭证，审定作“生物”；非审定公布库）',
         '2026-11-18 JWT 直连凭证，作“生物”；非审定公布库，2026-11-26 索引复核）'),
    ],
    'center of oscillation': [
        ('亦作记审定·物理学作“摆动中心”',
         '亦作记%s·测绘学作“摆动中心”（center of oscillation of pendulum，非审定公布库，'
         '2026-11-26 索引复核）' % TW),
    ],
    'lunar inequality': [
        ('亦作记审定·天文学作“月行差”',
         '亦作记%s·测绘学作“月行差”（lunar inequality; evection，非审定公布库，'
         '2026-11-26 索引复核）' % TW),
    ],
    'accidental generalization': [
        ('审定名词库（termonline-all·自然辩证法名词，2026-11-11 浏览器通道凭证）',
         '审定作“偶适概括”（accidental regularities; uniformities; generalizations，'
         '自然辩证法名词 03.210；英文列为近义并列形，2026-11-26 索引复核）'),
    ],
    'action quantum': [
        ('审定名词库（termonline-all·物理学名词·量子理论，2026-11-08 浏览器通道凭证，'
         'en=quantum of action 精确命中）',
         '审定作“量子作用”（quantum of action，物理学名词 06.0375；英文为异序形，'
         '2026-11-26 索引复核）'),
    ],
    'evolutionary game theory': [
        ('审定名词（经济学名词通行）；凭证 2026-11-07',
         '审定库首屏无该键配对条目（构成词在案：“博弈论”对 game theory，自然辩证法名词 03.796；'
         '“进化论”对 evolutionary theory，03.418；复合词未收，2026-11-26 索引复核）；凭证 2026-11-07'),
    ],
    'free speech': [
        ('审定库复核一致（termonline-all 浏览器通道凭证 2026-10-29；2026-11-25 界面精确匹配复核在案）',
         '审定作“言论自由”（freedom of speech，新闻学与传播学名词 17.054；英文与 free speech 异形，'
         '2026-11-26 索引复核）'),
    ],
    'Stoic': [
        ('审定名词库（termonline-all·自然辩证法/世界历史名词，2026-11-11 浏览器通道凭证）',
         '审定作“斯多葛学派”（Stoics，自然辩证法名词 02.142）、“斯多葛派”（Stoics，'
         '世界历史名词 02.0388）（2026-11-26 索引复核）'),
    ],
    'śūnyatā': [
        ('审定名词库（termonline-all·哲学，2026-10-31 浏览器通道凭证）',
         '%s“中华思想文化术语传播工程”作“空”（Śūnyatā / Emptiness）；审定公布库无该条'
         '（2026-11-26 索引复核）' % OTHER),
    ],
}


def fix_basis(key, basis):
    """按 LIBFIX／SPECIAL 改依据串，返回新串或 None（无改动）。"""
    out = basis
    if key in LIBFIX:
        lib = LIBFIX[key]
        old = '审定名词库（termonline-all·'
        if old not in out:
            raise SystemExit('%s 缺通用句式，中止' % key)
        out = out.replace(old, '%s（termonline-all·' % lib, 1)
        out = out.replace('，审定作“', '，作“')
        out = out.replace('；审定“', '；%s“' % ('对照库' if lib == TW else '其他库'))
        out = out.replace('2026-11-18 JWT 直连凭证）',
                          '2026-11-18 JWT 直连凭证；非审定公布库，2026-11-26 索引复核）')
    for old, new in SPECIAL.get(key, ()):
        if old not in out:
            raise SystemExit('%s 旧串未找到，中止：%r' % (key, old[:40]))
        out = out.replace(old, new, 1)
    return out if out != basis else None


def main():
    keys = set(LIBFIX) | set(SPECIAL)
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8:
                key = cells[1].strip()
                if key in keys:
                    new = fix_basis(key, cells[5])
                    if new is None:
                        raise SystemExit('%s 无实质改动' % key)
                    cells[5] = new
                    cells[6] = ' %s ' % DATE
                    done.add(key)
                    line = '|'.join(cells)
        out.append(line)
    missing = keys - done
    if missing:
        raise SystemExit('漏改 %d 行：%s' % (len(missing), '、'.join(sorted(missing))))
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 %d 行（库名失实 %d／裸断言写实 %d，有重叠）' % (len(done), len(LIBFIX), len(SPECIAL)))


if __name__ == '__main__':
    main()

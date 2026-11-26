# -*- coding: utf-8 -*-
"""批 68：术语表首现与正文实况核对（2026-11-26）。

判据：首现条目必须**真含该词**。全量扫 en/ 下每个词条的 index/notes/supplement/
further-discussion 等全部 HTML（Unicode NFC 归一、小写），逐键精确匹配；同形但语义不同者
（kevala-vyatirekin 的 kevala=“唯”、Tapasyananda 人名）不算命中。

两类处置：
* **改记**（词在别的条目）：coproduct／sheaf → category-theory；Hesychast →
  byzantine-philosophy；Proslogion → anselm；Silhak → korean-confucianism（本库作
  Sirhak）；Träume eines Geistersehers → dreams-dreaming。
* **待核**（全库无该词，或仅见异义形）：耆那系 13 行＋foliation、erotapokriseis、
  Ewam Choden、kalokagathos、Zahlfiguren。首现改成说明性标注，依据列留核查口径，
  词条译出后再回填。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TABLE = 'shu-yu-biao.md'
DATE = '2026-11-26'

POINTER = '2026-11-26 核：原记首现词条正文未见该词，按全库精确匹配改记'
JAINA_NOTE = ('2026-11-26 核：全库正文（index/notes/supplement/further-discussion 等全部 '
              'HTML，NFC 归一）未见该词；jaina-philosophy 行文用 omniscience 等通名，'
              '本行术语系按耆那研究通行形登记，首现待该条译出后回填')

FIX = {
    # ---- 改记：词在别的条目 ----
    'coproduct': ('category-theory',
                  POINTER + '（category-theory；axiom-choice 补编亦见）'),
    'sheaf': ('category-theory',
              POINTER + '（category-theory；axiom-choice 补编亦见）'),
    'Hesychast': ('byzantine-philosophy',
                  POINTER + '（byzantine-philosophy、medieval-philosophy 两见，取字母序首条）'),
    'Proslogion': ('anselm',
                   POINTER + '（anselm、bonaventure、christiantheology-philosophy 等见）'),
    'Silhak(實學)': ('korean-confucianism',
                     POINTER + '（本库作 Sirhak，korean-confucianism；Silhak 拼形未见）'),
    'Träume eines Geistersehers': ('dreams-dreaming',
                                   POINTER + '（dreams-dreaming，另 bloch、friedrich-jacobi 引及）'),
    # ---- 待核：全库无该词或仅见异义形 ----
    'aṇuvrata': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'avadhi-jñāna': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'avaktavya': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'guṇasthāna': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'kevala': ('待核（jaina-philosophy 正文未见原词）',
               JAINA_NOTE + '；本库仅见 kevala-vyatirekin 等因明复合形，非全知义'),
    'kevalin': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'lesyā': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'mahāvrata': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'mati-jñāna': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'sāgaropama': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'saptabhaṅgī': ('待核（jaina-philosophy 正文未见原词）', JAINA_NOTE),
    'śruta-jñāna': ('待核（jaina-philosophy 正文未见原词）',
                    JAINA_NOTE + '；本库 śruta 仅见 tsongkhapa（藏传“闻”义）'),
    'tapas': ('待核（jaina-philosophy 正文未见原词）',
              JAINA_NOTE + '；本库仅见 Tapasyananda 人名等字符串，无苦行义'),
    'foliation': ('待核（本库仅见波姆力学用法）',
                  '2026-11-26 核：spacetime-convensimul 正文未见该词；本库 foliation 见于 '
                  'qm-bohm、quantum-gravity 等（波姆力学/量子引力用法），与微分几何义不同，'
                  '首现待几何条译出后回填'),
    'erotapokriseis': ('待核（john-italos 正文未见原词）', POINTER + '（全库未见）'),
    'Ewam Choden': ('待核（gorampa 正文未见原词）', POINTER + '（全库未见）'),
    'kalokagathos': ('待核（landmann-kalischer 正文未见原词）', POINTER + '（全库未见）'),
    'Zahlfiguren': ('待核（ehrenfels 正文未见原词）', POINTER + '（全库未见）'),
}


def main():
    lines = io.open(TABLE, encoding='utf-8', newline='').read().split('\n')
    out, done = [], set()
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 7 and cells[1].strip() in FIX:
                key = cells[1].strip()
                new, note = FIX[key]
                if cells[4].strip() != new:
                    cells[4] = ' %s ' % new
                if note not in cells[5]:
                    cells[5] = cells[5].rstrip() + '；' + note + ' '
                cells[6] = ' %s ' % DATE
                done.add(key)
                line = '|'.join(cells)
        out.append(line)
    missing = set(FIX) - done
    if missing:
        raise SystemExit('漏改：%s' % '、'.join(sorted(missing)))
    io.open(TABLE, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改 %d 行（改记 %d／待核 %d）'
          % (len(done), len([k for k, v in FIX.items() if not v[0].startswith('待核')]),
             len([k for k, v in FIX.items() if v[0].startswith('待核')])))


if __name__ == '__main__':
    main()

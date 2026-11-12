# -*- coding: utf-8 -*-
"""mu-lu-s 哲学史重分类映射器（specs/016）。

只读 mu-lu-s.md，输出 results/mapping.tsv：
  slug, title, current_section, new_section, sort_key, confidence, note

规则：
  1. SLUG_SECTION 显式指定者优先；
  2. 否则按现节 fallback（HISTORY_FALLBACK）；
  3. 哲学通论条目默认保留原节，除非在 MOVE_FROM_TOPIC 中。
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SRC = os.path.join(ROOT, 'mu-lu-s.md')
OUT = os.path.join(ROOT, 'specs', '016-mulu-history-recategorize', 'results', 'mapping.tsv')

W = '西方哲学史'
E = '欧美以外哲学史'

S = {
    # 古代
    'A11': f'{W} > 一、古代哲学 > 1.1 早期希腊自然哲学 > 伊奥尼亚哲学',
    'A12': f'{W} > 一、古代哲学 > 1.1 早期希腊自然哲学 > 南意大利哲学',
    'A13': f'{W} > 一、古代哲学 > 1.1 早期希腊自然哲学 > 多元论与原子论',
    'A21': f'{W} > 一、古代哲学 > 1.2 古典希腊哲学 > 智者运动',
    'A22': f'{W} > 一、古代哲学 > 1.2 古典希腊哲学 > 苏格拉底',
    'A23': f'{W} > 一、古代哲学 > 1.2 古典希腊哲学 > 小苏格拉底学派',
    'A24': f'{W} > 一、古代哲学 > 1.2 古典希腊哲学 > 柏拉图与学园',
    'A25': f'{W} > 一、古代哲学 > 1.2 古典希腊哲学 > 亚里士多德与逍遥学派',
    'A31': f'{W} > 一、古代哲学 > 1.3 晚期希腊与罗马哲学 > 伊壁鸠鲁主义',
    'A32': f'{W} > 一、古代哲学 > 1.3 晚期希腊与罗马哲学 > 斯多亚学派',
    'A33': f'{W} > 一、古代哲学 > 1.3 晚期希腊与罗马哲学 > 怀疑主义与新学园',
    'A34': f'{W} > 一、古代哲学 > 1.3 晚期希腊与罗马哲学 > 新柏拉图主义',
    'A35': f'{W} > 一、古代哲学 > 1.3 晚期希腊与罗马哲学 > 罗马哲学与拜占庭',
    'A9': f'{W} > 一、古代哲学 > 1.4 古代哲学专题',
    # 中古
    'M11': f'{W} > 二、中古哲学 > 2.1 思想来源与教父哲学 > 希腊护教士与亚历山大里亚学派',
    'M12': f'{W} > 二、中古哲学 > 2.1 思想来源与教父哲学 > 拉丁护教士',
    'M13': f'{W} > 二、中古哲学 > 2.1 思想来源与教父哲学 > 奥古斯丁',
    'M14': f'{W} > 二、中古哲学 > 2.1 思想来源与教父哲学 > 伪狄奥尼修斯与波爱修',
    'M21': f'{W} > 二、中古哲学 > 2.2 奥古斯丁主义与黑暗时代 > 奥古斯丁主义',
    'M22': f'{W} > 二、中古哲学 > 2.2 奥古斯丁主义与黑暗时代 > 加洛林文艺复兴与爱留根纳',
    'M31': f'{W} > 二、中古哲学 > 2.3 经院哲学的诞生（11–12世纪） > 安瑟伦与早期经院',
    'M32': f'{W} > 二、中古哲学 > 2.3 经院哲学的诞生（11–12世纪） > 阿伯拉尔与12世纪',
    'M41': f'{W} > 二、中古哲学 > 2.4 亚里士多德主义的传播（12–13世纪） > 阿拉伯与犹太中介',
    'M42': f'{W} > 二、中古哲学 > 2.4 亚里士多德主义的传播（12–13世纪） > 拉丁阿维罗伊主义',
    'M51': f'{W} > 二、中古哲学 > 2.5 经院哲学的兴盛（13世纪） > 大阿尔伯特与阿奎那',
    'M52': f'{W} > 二、中古哲学 > 2.5 经院哲学的兴盛（13世纪） > 波纳文图拉与方济各传统',
    'M61': f'{W} > 二、中古哲学 > 2.6 经院哲学的分裂（13世纪末–14世纪） > 1277年谴责',
    'M62': f'{W} > 二、中古哲学 > 2.6 经院哲学的分裂（13世纪末–14世纪） > 司各脱主义',
    'M63': f'{W} > 二、中古哲学 > 2.6 经院哲学的分裂（13世纪末–14世纪） > 奥康主义与“现代路线”',
    'M64': f'{W} > 二、中古哲学 > 2.6 经院哲学的分裂（13世纪末–14世纪） > 中世纪神秘主义',
    'M65': f'{W} > 二、中古哲学 > 2.6 经院哲学的分裂（13世纪末–14世纪） > 唯名论与实在论之争',
    'M33': f'{W} > 二、中古哲学 > 2.3 经院哲学的诞生（11–12世纪） > 理性与信仰之争',
    'M71': f'{W} > 二、中古哲学 > 2.7 中世纪晚期（14–16世纪） > 牛津计算学派',
    'M72': f'{W} > 二、中古哲学 > 2.7 中世纪晚期（14–16世纪） > 威克里夫与宗教改革前夜',
    'M8': f'{W} > 二、中古哲学 > 2.8 拜占庭哲学',
    'M9': f'{W} > 二、中古哲学 > 2.9 中世纪哲学专题',
    # 文艺复兴
    'R1': f'{W} > 三、文艺复兴与宗教改革（1350–1600） > 3.1 人文主义与政治哲学',
    'R21': f'{W} > 三、文艺复兴与宗教改革（1350–1600） > 3.2 古典哲学的复兴 > 柏拉图主义',
    'R22': f'{W} > 三、文艺复兴与宗教改革（1350–1600） > 3.2 古典哲学的复兴 > 亚里士多德主义',
    'R23': f'{W} > 三、文艺复兴与宗教改革（1350–1600） > 3.2 古典哲学的复兴 > 斯多亚主义与怀疑主义',
    'R3': f'{W} > 三、文艺复兴与宗教改革（1350–1600） > 3.3 宗教改革',
    'R4': f'{W} > 三、文艺复兴与宗教改革（1350–1600） > 3.4 自然哲学与科学革命',
    # 近代
    'N10': f'{W} > 四、近代哲学（1600–1830） > 4.1 唯理论 > 唯理论总论',
    'N11': f'{W} > 四、近代哲学（1600–1830） > 4.1 唯理论 > 笛卡尔与笛卡尔学派',
    'N14': f'{W} > 四、近代哲学（1600–1830） > 4.1 唯理论 > 剑桥柏拉图学派',
    'N12': f'{W} > 四、近代哲学（1600–1830） > 4.1 唯理论 > 斯宾诺莎',
    'N13': f'{W} > 四、近代哲学（1600–1830） > 4.1 唯理论 > 莱布尼茨-沃尔夫学派',
    'N21': f'{W} > 四、近代哲学（1600–1830） > 4.2 经验论 > 培根与霍布斯',
    'N22': f'{W} > 四、近代哲学（1600–1830） > 4.2 经验论 > 洛克',
    'N23': f'{W} > 四、近代哲学（1600–1830） > 4.2 经验论 > 贝克莱',
    'N24': f'{W} > 四、近代哲学（1600–1830） > 4.2 经验论 > 休谟',
    'N25': f'{W} > 四、近代哲学（1600–1830） > 4.2 经验论 > 苏格兰常识学派',
    'N26': f'{W} > 四、近代哲学（1600–1830） > 4.2 经验论 > 英国道德哲学与宗教哲学',
    'N31': f'{W} > 四、近代哲学（1600–1830） > 4.3 启蒙运动 > 法国启蒙',
    'N32': f'{W} > 四、近代哲学（1600–1830） > 4.3 启蒙运动 > 苏格兰启蒙',
    'N33': f'{W} > 四、近代哲学（1600–1830） > 4.3 启蒙运动 > 德国启蒙',
    'N34': f'{W} > 四、近代哲学（1600–1830） > 4.3 启蒙运动 > 自然法与社会契约',
    'N35': f'{W} > 四、近代哲学（1600–1830） > 4.3 启蒙运动 > 法国唯物主义',
    'N36': f'{W} > 四、近代哲学（1600–1830） > 4.3 启蒙运动 > 德国通俗哲学',
    'N41': f'{W} > 四、近代哲学（1600–1830） > 4.4 德国古典哲学 > 康德',
    'N42': f'{W} > 四、近代哲学（1600–1830） > 4.4 德国古典哲学 > 费希特',
    'N43': f'{W} > 四、近代哲学（1600–1830） > 4.4 德国古典哲学 > 谢林',
    'N44': f'{W} > 四、近代哲学（1600–1830） > 4.4 德国古典哲学 > 黑格尔',
    'N5': f'{W} > 四、近代哲学（1600–1830） > 4.5 浪漫主义与人文科学',
    # 现代
    'C11': f'{W} > 五、现代哲学（1830–） > 5.1 后黑格尔与马克思主义 > 青年黑格尔派',
    'C12': f'{W} > 五、现代哲学（1830–） > 5.1 后黑格尔与马克思主义 > 马克思与恩格斯',
    'C13': f'{W} > 五、现代哲学（1830–） > 5.1 后黑格尔与马克思主义 > 西方马克思主义',
    'C21': f'{W} > 五、现代哲学（1830–） > 5.2 非理性主义与生存哲学 > 叔本华',
    'C22': f'{W} > 五、现代哲学（1830–） > 5.2 非理性主义与生存哲学 > 克尔凯郭尔',
    'C23': f'{W} > 五、现代哲学（1830–） > 5.2 非理性主义与生存哲学 > 尼采',
    'C31': f'{W} > 五、现代哲学（1830–） > 5.3 实证主义与科学主义 > 第一代实证主义',
    'C32': f'{W} > 五、现代哲学（1830–） > 5.3 实证主义与科学主义 > 马赫主义',
    'C33': f'{W} > 五、现代哲学（1830–） > 5.3 实证主义与科学主义 > 维也纳学派与逻辑实证主义',
    'C34': f'{W} > 五、现代哲学（1830–） > 5.3 实证主义与科学主义 > 功利主义与古典自由主义',
    'C4': f'{W} > 五、现代哲学（1830–） > 5.4 新康德主义与英国唯心论',
    'C41': f'{W} > 五、现代哲学（1830–） > 5.4 新康德主义与英国唯心论 > 新康德主义',
    'C42': f'{W} > 五、现代哲学（1830–） > 5.4 新康德主义与英国唯心论 > 英国唯心论',
    'C43': f'{W} > 五、现代哲学（1830–） > 5.4 新康德主义与英国唯心论 > 19世纪学院哲学',
    'C5': f'{W} > 五、现代哲学（1830–） > 5.5 现象学运动',
    'C6': f'{W} > 五、现代哲学（1830–） > 5.6 存在主义与解释学',
    'C61': f'{W} > 五、现代哲学（1830–） > 5.6 存在主义与解释学 > 存在主义',
    'C62': f'{W} > 五、现代哲学（1830–） > 5.6 存在主义与解释学 > 解释学',
    'C71': f'{W} > 五、现代哲学（1830–） > 5.7 分析哲学 > 早期分析哲学',
    'C72': f'{W} > 五、现代哲学（1830–） > 5.7 分析哲学 > 日常语言哲学',
    'C73': f'{W} > 五、现代哲学（1830–） > 5.7 分析哲学 > 后实证科学哲学',
    'C74': f'{W} > 五、现代哲学（1830–） > 5.7 分析哲学 > 分析形而上学与语言哲学',
    'C75': f'{W} > 五、现代哲学（1830–） > 5.7 分析哲学 > 分析伦理学与政治哲学',
    'C8': f'{W} > 五、现代哲学（1830–） > 5.8 批判理论',
    'C9': f'{W} > 五、现代哲学（1830–） > 5.9 结构主义与后结构主义',
    'C10': f'{W} > 五、现代哲学（1830–） > 5.10 实用主义与过程哲学',
    'C11p': f'{W} > 五、现代哲学（1830–） > 5.11 政治哲学与法哲学',
    # 犹太
    'J1': f'{W} > 六、犹太哲学（跨期传统） > 6.1 古代与中世纪犹太哲学',
    'J2': f'{W} > 六、犹太哲学（跨期传统） > 6.2 近代犹太哲学',
    'J3': f'{W} > 六、犹太哲学（跨期传统） > 6.3 现代犹太哲学',
    # 区域
    'CH1': f'{E} > 中国哲学 > 先秦',
    'CH2': f'{E} > 中国哲学 > 汉唐',
    'CH3': f'{E} > 中国哲学 > 宋明',
    'CH4': f'{E} > 中国哲学 > 清代',
    'CH5': f'{E} > 中国哲学 > 现代',
    'CH6': f'{E} > 中国哲学 > 中国佛教',
    'CH7': f'{E} > 中国哲学 > 藏传佛教',
    'CH8': f'{E} > 中国哲学 > 道教',
    'CH9': f'{E} > 中国哲学 > 专题',
    'IN1': f'{E} > 印度哲学 > 佛教',
    'IN2': f'{E} > 印度哲学 > 耆那教',
    'IN3': f'{E} > 印度哲学 > 正理-胜论',
    'IN4': f'{E} > 印度哲学 > 弥曼差',
    'IN5': f'{E} > 印度哲学 > 不二吠檀多',
    'IN6': f'{E} > 印度哲学 > 早期现代',
    'IN7': f'{E} > 印度哲学 > 专题',
    'JP1': f'{E} > 日本哲学 > 古代与中世',
    'JP2': f'{E} > 日本哲学 > 近世',
    'JP3': f'{E} > 日本哲学 > 近代',
    'JP4': f'{E} > 日本哲学 > 专题',
    'KR1': f'{E} > 韩国哲学 > 儒学',
    'KR2': f'{E} > 韩国哲学 > 佛教',
    'KR3': f'{E} > 韩国哲学 > 通论',
    'IS1': f'{E} > 伊斯兰哲学 > 早期',
    'IS2': f'{E} > 伊斯兰哲学 > 黄金时代',
    'IS3': f'{E} > 伊斯兰哲学 > 后期',
    'IS4': f'{E} > 伊斯兰哲学 > 专题',
    'AF1': f'{E} > 非洲与非裔哲学 > 传统非洲哲学',
    'AF2': f'{E} > 非洲与非裔哲学 > 非裔哲学',
    'AF3': f'{E} > 非洲与非裔哲学 > 当代',
    'LA1': f'{E} > 拉丁美洲哲学 > 19–20世纪',
    'LA2': f'{E} > 拉丁美洲哲学 > 专题',
}


def parse_slugs(text):
    return [x for x in re.split(r'[\s,]+', text.strip()) if x]


ASSIGN = {}


def put(key, text):
    for slug in parse_slugs(text):
        ASSIGN[slug] = S[key]


put('A11', '''
presocratics doxography-ancient heraclitus
''')
put('A12', '''
pythagoras philolaus pythagoreanism alcmaeon archytas xenophanes parmenides zeno-elea paradox-zeno
''')
put('A13', '''
empedocles anaxagoras atomism-ancient leucippus democritus
''')
put('A21', '''
sophists protagoras callicles-thrasymachus
''')
put('A22', 'socrates')
put('A23', '''
cyrenaics dialectical-school diodorus-cronus
''')
put('A24', '''
plato plato-cratylus plato-ethics plato-ethics-politics plato-friendship plato-laws
plato-sophstate plato-metaphysics plato-myths plato-theaetetus plato-parmenides
plato-rhetoric plato-ethics-shorter plato-timaeus plato-aesthetics speusippus xenocrates
''')
put('A25', '''
aristotle aristotle-aesthetics aristotle-biology aristotle-categories aristotle-ethics
aristotle-logic aristotle-metaphysics aristotle-politics aristotle-psychology
aristotle-rhetoric aristotle-mathematics aristotle-causality aristotle-de-motu
aristotle-text aristotle-natphil aristotle-noncontradiction aristotle-commentators theophrastus
''')
put('A31', 'epicurus philodemus lucretius')
put('A32', 'stoicism marcus-aurelius epictetus seneca')
put('A33', '''
pyrrho timon-phlius sextus-empiricus arcesilaus carneades philo-larissa
''')
put('A34', '''
neoplatonism plotinus porphyry iamblichus plutarch syrianus proclus ammonius
simplicius numenius antiochus-ascalon olympiodorus david elias
''')
put('A35', 'cicero galen alexander-aphrodisias')
put('A9', 'ancient-soul freedom-ancient intentionality-ancient skepticism-ancient logic-ancient ethics-ancient ancient-political episteme-techne')

put('M11', 'origen')
put('M13', 'augustine')
put('M14', 'pseudo-dionysius-areopagite boethius')
put('M22', 'scottus-eriugena')
put('M31', 'anselm peter-damian')
put('M32', '''
abelard william-champeaux john-salisbury alberic-paris peter-spain
''')
put('M42', 'boethius-dacia')
put('M51', '''
albert-great aquinas aquinas-moral-political william-auvergne giles henry-ghent
philip-chancellor roger-bacon grosseteste llull radulphus-brito simon-faversham
''')
put('M52', 'bonaventure olivi')
put('M61', 'condemnation robert-kilwardby godfrey')
put('M62', 'duns-scotus medieval-haecceity modality-medieval')
put('M63', '''
ockham walter-chatton crathorn francis-marchia gregory-rimini wodeham dietrich-freiberg
''')
put('M71', '''
heytesbury kilvington albert-saxony nicole-oresme buridan marsilius-inghen
''')
put('M72', '''
wyclif wyclif-political marsilius-padua medieval-political james-viterbo fitzralph
''')
put('M8', 'byzantine-philosophy john-italos philoponus joane-petrizi')
put('M9', '''
medieval-philosophy medieval-literary analogy-medieval representation-medieval
arabic-islamic-essence
''')

put('R1', '''
dante erasmus machiavelli montaigne bodin thomas-more lorenzo-valla vives
justus-lipsius lefevre-etaples
''')
put('R21', '''
cusanus bessarion ficino pico-della-mirandola gianfrancesco-pico patrizi
''')
put('R22', '''
pomponazzi zabarella suarez school-salamanca gomez-pereira aristotelianism-renaissance taurellus
''')
put('R3', 'luther luther-influence')
put('R4', '''
natphil-ren copernicus bruno telesio cardano kepler galileo francisco-sanches
campanella della-porta agrippa
''')

put('N11', '''
descartes descartes-epistemology descartes-works descartes-mathematics descartes-method
descartes-modal descartes-ontological descartes-physics descartes-ideas descartes-ethics
pineal-gland clauberg cordemoy la-forge desgabets legrand henricus-regius arnauld
mersenne pascal pascal-wager john-norris francois-barre johann-sturm clarke
malebranche malebranche-ideas
''')
put('N12', '''
spinoza spinoza-epistemology-mind spinoza-modal spinoza-physics spinoza-political
spinoza-psychological spinoza-attributes
''')
put('N10', 'continental-rationalism rationalism-early-modern')
put('N13', '''
leibniz leibniz-ethics leibniz-exoteric leibniz-logic-influence leibniz-modal
leibniz-causation leibniz-evil leibniz-mind leibniz-physics sufficient-reason
wolff-christian
''')
put('N14', 'cambridge-platonists cudworth henry-more conway')
put('N21', 'francis-bacon hobbes hobbes-moral hobbes-science margaret-cavendish')
put('N22', '''
locke locke-moral locke-freedom locke-personal-identity locke-philosophy-science
locke-political locke-on-medicine real-essence
''')
put('N23', 'berkeley')
put('N24', '''
hume hume-moral hume-newton hume-freewill hume-religion hume-aesthetics
''')
put('N25', 'reid reid-ethics reid-memory-identity scottish-18th')
put('N26', 'hartley collins butler-moral cockburn margaret-fell')
put('N31', '''
montesquieu voltaire rousseau diderot holbach condillac du-bos bayle gassendi
''')
put('N32', '''
hutcheson smith-moral-political mandeville shaftesbury edwards
''')
put('N33', '''
18thGerman-preKant mendelssohn jacobi hamann
''')
put('N34', 'grotius pufendorf burke paine jefferson richard-price')
put('N41', '''
kant kant-leibniz kant-development kant-judgment innateness-history analytic-synthetic
transcendental-arguments apriori kant-transcendental kant-reason kant-conceptualism
kant-metaphysics kant-hume-causality kant-hume-morality kant-moral kant-mathematics
kant-religion kant-science kant-social-political kant-transcendental-idealism
kant-mind kant-spacetime kant-aesthetics schema practical-reason persons-means
''')
put('N42', 'johann-fichte karl-reinhold august-rehberg')
put('N43', 'schelling')
put('N44', '''
hegel hegel-dialectics hegel-social-political hegel-aesthetics friedrich-jacobi
''')
put('N5', '''
novalis schlegel schlegel-aw schiller schleiermacher personalism wilhelm-humboldt
herder vico
''')

put('C11', 'max-stirner bauer ludwig-feuerbach')
put('C12', 'marx engels')
put('C13', 'marxism-analytical gramsci lukacs bloch althusser')
put('C21', 'schopenhauer schopenhauer-aesthetics')
put('C22', 'kierkegaard')
put('C23', 'nietzsche nietzsche-life-works nietzsche-moral-political nietzsche-aesthetics')
put('C31', 'comte spencer whewell alexander-humboldt')
put('C32', 'ernst-mach')
put('C33', '''
vienna-circle ayer carnap feigl neurath schlick hempel reichenbach physics-Rpcc
''')
put('C73', 'popper feyerabend fleck thomas-kuhn lakatos wesley-salmon duhem')
put('C71', 'brouwer goedel church')
put('C33', 'poincare')
put('C74', 'weyl')
put('N11', 'consciousness-17th emotions-17th18th qualities-prim-sec occasionalism port-royal-logic')
put('C34', '''
utilitarianism-history bentham godwin mill mill-moral-political sidgwick james-mill
''')
put('C4', '''
james-ward fechner wilhelm-wundt neo-kantianism friedrich-lange natorp
wilhelm-windelband cohen heinrich-rickert green bosanquet bradley bradley-moral
bradley-regress dilthey cassirer vaihinger collingwood collingwood-aesthetics
findlay mctaggart alexander whitehead process-philosophy process-theism hartshorne
anderson-john hermann-lotze
''')
put('C5', '''
brentano brentano-judgement ehrenfels stumpf twardowski meinong phenomenology
phenomenology-mg reinach husserl heidegger heidegger-aesthetics ingarden scheler
schutz michel-henry merleau-ponty
''')
put('C6', '''
existentialism existentialism-mexican camus jaspers marcel sartre authenticity
gasset hermeneutics gadamer gadamer-aesthetics ricoeur yorck levinas bergson
''')
put('C71', '''
frege frege-logic frege-hilbert frege-theorem moore moore-moral ramsey
ramsey-economics russell russell-moral russell-paradox logical-atomism
logical-construction descriptions principia-mathematica pm-notation lvov-warsaw
lukasiewicz tarski tarski-truth wittgenstein wittgenstein-atomism
wittgenstein-mathematics wittgenstein-aesthetics lesniewski
''')
put('C72', 'strawson ryle austin-jl grice')
put('C74', '''
quine quine-nf davidson lewis-metaphysics williams-dc sellars sylvan-routley
chisholm goodman goodman-aesthetics williams-bernard broad
''')
put('C75', 'hare prichard william-david-ross stevenson berlin')
put('C8', 'adorno marcuse horkheimer benjamin habermas critical-theory')
put('C9', 'baudrillard deleuze foucault lyotard postmodernism derrida lacan')
put('C10', '''
pragmatism dewey dewey-moral dewey-political dewey-aesthetics sidney-hook james
lewis-ci mead rorty santayana transcendentalism thoreau emerson peirce
peirce-logic peirce-semiotics peirce-benjamin royce wright
''')
put('C11p', 'rawls nozick-political oakeshott schmitt strauss-leo weber socialism capitalism rationality-instrumental')
put('C74', 'linguistics')

put('J1', '''
philo saadya halevi maimonides maimonides-islamic gersonides crescas abrabanel
albo-joseph abner-burgos ibn-ezra abraham-daud falaquera tibbon israeli polqar
ibn-gabirol albalag kaspi-joseph
''')
put('J2', 'maimon mendelssohn')
put('J3', 'buber rosenzweig scholem leibowitz-yeshayahu')

put('CH1', 'confucius laozi mencius xunzi zhuangzi school-names chinese-legalism mohism mohist-canons')
put('CH9', 'chinese-change')
put('CH2', 'neo-daoism han-dynasty')
put('CH3', 'song-ming-confucianism wang-yangming zhu-xi')
put('CH4', 'qing-philosophy dai-zhen')
put('CH5', 'confucianism-modern')
put('CH6', 'buddhism-chan buddhism-huayan buddhism-tiantai')
put('CH7', '''
gelukpa gorampa sakya-pandita epistemology-language-tibetan tsongkhapa twotruths-tibet
''')
put('CH8', 'daoism daoism-religion')
put('CH9', '''
chinese-phil-medicine chinese-painting-calligraphy chinese-phil-science
chinese-epistemology chinese-metaphysics chinese-social-political
chinese-translate-interpret comparphil-chiwes emotions-chinese
chinese-logic-language ethics-chinese confucian-gender chinese-mind
''')

put('IN1', '''
buddha abhidharma madhyamaka yogacara dharmakiirti ratnakirti srigupta nagarjuna
saantarak-sita shantideva vasubandhu ethics-indian-buddhism mind-indian-buddhism
twotruths-india
''')
put('IN2', 'jaina-philosophy jayaraasi')
put('IN3', 'gangesa')
put('IN4', 'kumaarila')
put('IN5', 'shankara')
put('IN6', 'early-modern-india')
put('IN7', '''
concept-emotion-india epistemology-india language-india literal-nonliteral-india
logic-india naturalism-india perception-india personhood-india sriharsa sikh-philosophy
''')

put('JP1', 'kukai')
put('JP2', 'japanese-confucian kokugaku-school')
put('JP3', 'kyoto-school nishida-kitaro watsuji-tetsuro')
put('JP4', 'japanese-philosophy japanese-aesthetics japanese-pure-land japanese-zen')

put('KR1', 'korean-confucianism')
put('KR2', 'korean-buddhism')
put('KR3', 'korean-philosophy')

put('IS1', 'al-kindi al-razi al-farabi al-farabi-metaphysics al-farabi-logic al-farabi-soc-rel al-farabi-psych')
put('IS2', '''
ibn-sina ibn-sina-logic ibn-sina-metaphysics ibn-sina-natural al-ghazali
ibn-rushd ibn-rushd-natural ibn-bajja
''')
put('IS3', '''
suhrawardi mulla-sadra ibn-arabi ibn-taymiyya al-qudat al-khunaji al-din-al-razi
al-baghdadi
''')
put('IS4', '''
arabic-islamic-metaphysics arabic-islamic-natural arabic-islamic-language
arabic-islamic-phil-math arabic-islamic-religion arabic-islamic-mind
arabic-islamic-greek arabic-islamic-judaic arabic-islamic-influence
arabic-islamic-mysticism arabic-islamic-causation arabic-islamic-liar
theology-aristotle umar-khayyam
''')

put('AF1', 'african-ethics african-sage akan-person shaaban-robert-ethics')
put('AF2', '''
africana alain-locke frantz-fanon negritude dubois frederick-douglass
double-consciousness anna-julia-cooper alexander-crummell
''')
put('AF3', 'africana-contemporary')

put('LA1', '''
philosophy-chile philosophy-mexico latin-american-philosophy latin-american-analytic
latin-american-metaphilosophy epistemology-latin-america latinx
''')
put('LA2', '''
phil-bio-latin-america phil-science-latin-america skepticism-latin-america
bioethics-latin-america feminism-latin-america liberalism-latin-america
existentialism-mexican liberation
''')

# 哲学通论中需要移出的人物（人物册与散落）
put('C71', 'prior scholz mally bolzano boole wilson')
put('M32', 'lambert-auxerre richard-sophister william-sherwood')
put('R1', 'ramus')
put('C4', 'johann-herbart')
put('R4', 'galileo')
put('N13', 'boyle newton')
put('C4', 'hermann-helmholtz')
put('C34', 'william-jevons')
put('C11p', 'friedrich-hayek')
put('N34', 'pufendorf')
put('C11p', 'maritain antonio-rosmini')
put('R22', 'taurellus')
put('R4', 'della-porta agrippa-nettesheim')
put('M63', 'meister-eckhart')
put('M9', 'illumination binarium medieval-syllogism medieval-terms universals-medieval consequence-medieval demonstration-medieval insolubles sophismata semiotics-medieval probability-medieval-renaissance medieval-categories medieval-mereology relations-medieval transcendentals-medieval causation-medieval conscience-medieval practical-reason-med singular-terms-medieval medieval-emotions medieval-futcont obligationes')
put('N11', 'descartes')  # no-op, keeps explicit
put('C4', 'montessori-maria')
put('C74', 'langer beardsley-aesthetics david-lewis')
put('C5', 'landmann-kalischer')

put('C74', 'price')
put('C75', 'anscombe philippa-foot murdoch')
put('C11p', 'arendt')
put('C71', 'emily-elizabeth-constance-jones ruth-barcan-marcus stebbing')
put('C13', 'luxemburg')
put('C34', 'harriet-mill')
put('C4', 'george-eliot croce-aesthetics scottish-19th mary-shepherd')
put('C11p', 'ayn-rand addams-jane')
put('C5', 'stein')
put('C6', 'susman-margarete simone-weil beauvoir')
put('C10', 'fuller-margaret')
put('N34', 'wollstonecraft catharine-macaulay sophie-de-grouchy')
put('N11', 'elisabeth-bohemia')
put('N13', 'emilie-du-chatelet')

put('N11', 'astell')
put('N22', 'lady-masham')
put('R1', 'lucrezia-marinella madeleine-scudery')

# 现节 fallback
HISTORY_FALLBACK = {
    '早期希腊哲学（前苏格拉底哲学）': 'A11',
    '中期希腊哲学': 'A24',
    '晚期希腊哲学': 'A34',
    '教父哲学与早期经院哲学（100-700）': 'M11',
    '中世纪哲学通论': 'M9',
    '经院哲学（1000——1350）': 'M51',
    '文艺复兴与早期近代哲学 1350-1600': 'R1',
    '启蒙运动和早期现代哲学 1600-1750': 'N11',
    '近代女性哲学家（1500-1750）': 'N11',
    '19 世纪西方哲学 1750-1900': 'C4',
    '20 世纪西方哲学 1900—': 'C71',
    '现代女性哲学家（1750+）': 'C71',
    '马克思主义与西方马克思主义': 'C13',
    '中国哲学': 'CH9',
    '犹太哲学': 'J1',
    '非裔哲学': 'AF2',
    '印度哲学': 'IN7',
    '日本哲学': 'JP3',
    '韩国哲学': 'KR3',
    '拉丁美洲哲学': 'LA1',
    '伊斯兰哲学': 'IS4',
}


def main():
    lines = open(SRC, encoding='utf-8').read().splitlines()
    cur1 = cur2 = cur3 = None
    stack = []  # (indent, slug)
    rows = []
    for ln in lines:
        m = re.match(r'^(#{1,3})\s+(.*)$', ln)
        if m:
            lvl = len(m.group(1)); t = m.group(2).strip()
            if lvl == 1:
                cur1 = t; cur2 = cur3 = None
            elif lvl == 2:
                cur2 = t; cur3 = None
            elif lvl == 3:
                cur3 = t
            continue
        m = re.search(r'\[(.*?)\]\(([^)]*\.md)\)', ln)
        if not m:
            continue
        title, path = m.group(1), m.group(2)
        slug = path.split('/')[-1][:-3]
        indent = len(ln) - len(ln.lstrip(' '))
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1] if stack else ''
        stack.append((indent, slug))
        cur = cur3 or cur2 or cur1 or ''
        if slug in ASSIGN:
            new = ASSIGN[slug]
        elif cur1 in ('前言', '关于'):
            new = cur1
        elif cur2 in HISTORY_FALLBACK:
            new = S[HISTORY_FALLBACK[cur2]]
        else:
            new = f'{cur1} > {cur2}' + (f' > {cur3}' if cur3 else '')
        rows.append((slug, title, cur, new, parent))
    with open(OUT, 'w', encoding='utf-8', newline='') as f:
        f.write('slug\ttitle\tcurrent_section\tnew_section\tparent\tnote\n')
        for slug, title, cur, new, parent in rows:
            f.write(f'{slug}\t{title}\t{cur}\t{new}\t{parent}\t\n')
    print('rows', len(rows))
    print('assigned', sum(1 for r in rows if r[0] in ASSIGN))
    print('out', OUT)


if __name__ == '__main__':
    main()

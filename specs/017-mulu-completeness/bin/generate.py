# -*- coding: utf-8 -*-
"""017 生成器：按新骨架重排 mu-lu-s.md。

设计原则
--------
1. 骨架（SKELETON）是唯一的结构事实源：节名、层级、顺序。
2. 旧节到新节默认按“叶子标题同名”自动映射；改名、拆分、合并走 SECTION_MAP。
3. 单条目的跨节调整走 ITEM_MAP（slug → 新节）。
4. 不增删链接：输出前对账“输入的链接集合 == 输出的链接集合”。
5. 标题一律不带序号（用户裁定）。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "mu-lu-s.md"
OUT = ROOT / "mu-lu-s.md"

# ---------------------------------------------------------------- 骨架

W = "西方哲学史"
A = "古代哲学"
M = "中世纪哲学"
R = "文艺复兴与宗教改革"
E = "近代哲学"
N = "现代哲学"
J = "犹太哲学"

SKELETON: list[tuple[str, ...]] = [
    ("前言",),
    ("关于",),
    (W,),
    (W, A),
    (W, A, "早期希腊自然哲学"),
    (W, A, "早期希腊自然哲学", "伊奥尼亚哲学"),
    (W, A, "早期希腊自然哲学", "南意大利哲学"),
    (W, A, "早期希腊自然哲学", "多元论与原子论"),
    (W, A, "古典希腊哲学"),
    (W, A, "古典希腊哲学", "智者运动"),
    (W, A, "古典希腊哲学", "苏格拉底"),
    (W, A, "古典希腊哲学", "小苏格拉底学派"),
    (W, A, "古典希腊哲学", "柏拉图与学园"),
    (W, A, "古典希腊哲学", "亚里士多德与逍遥学派"),
    (W, A, "希腊化与罗马哲学"),
    (W, A, "希腊化与罗马哲学", "伊壁鸠鲁主义"),
    (W, A, "希腊化与罗马哲学", "斯多亚学派"),
    (W, A, "希腊化与罗马哲学", "怀疑主义与新学园"),
    (W, A, "希腊化与罗马哲学", "新柏拉图主义"),
    (W, A, "希腊化与罗马哲学", "罗马哲学与拜占庭"),
    (W, A, "古代哲学专题"),
    (W, M),
    (W, M, "思想来源与教父哲学"),
    (W, M, "思想来源与教父哲学", "希腊护教士与亚历山大里亚学派"),
    (W, M, "思想来源与教父哲学", "拉丁教父与奥古斯丁"),
    (W, M, "思想来源与教父哲学", "伪狄奥尼修斯与波爱修"),
    (W, M, "奥古斯丁主义与黑暗时代"),
    (W, M, "奥古斯丁主义与黑暗时代", "奥古斯丁主义"),
    (W, M, "奥古斯丁主义与黑暗时代", "加洛林文艺复兴与爱留根纳"),
    (W, M, "经院哲学的诞生"),
    (W, M, "经院哲学的诞生", "安瑟伦与理性主义神学"),
    (W, M, "经院哲学的诞生", "阿伯拉尔与共相之争"),
    (W, M, "经院哲学的诞生", "12 世纪人文与逻辑学派"),
    (W, M, "亚里士多德主义的传播"),
    (W, M, "亚里士多德主义的传播", "阿拉伯与犹太中介"),
    (W, M, "亚里士多德主义的传播", "拉丁阿维罗伊主义"),
    (W, M, "经院哲学的兴盛"),
    (W, M, "经院哲学的兴盛", "大阿尔伯特与托马斯主义"),
    (W, M, "经院哲学的兴盛", "波纳文图拉与方济各传统"),
    (W, M, "经院哲学的兴盛", "奥古斯丁主义复兴"),
    (W, M, "经院哲学的兴盛", "经院哲学的逻辑与自然哲学"),
    (W, M, "经院哲学的分裂"),
    (W, M, "经院哲学的分裂", "1277 年谴责"),
    (W, M, "经院哲学的分裂", "司各脱主义"),
    (W, M, "经院哲学的分裂", "唯名论与现代路线"),
    (W, M, "中世纪晚期"),
    (W, M, "中世纪晚期", "牛津计算学派"),
    (W, M, "中世纪晚期", "威克里夫与宗教改革前夜"),
    (W, M, "中世纪晚期", "德意志神秘主义"),
    (W, M, "拜占庭哲学"),
    (W, M, "中世纪哲学专题"),
    (W, R),
    (W, R, "人文主义与政治哲学"),
    (W, R, "古典哲学的复兴"),
    (W, R, "古典哲学的复兴", "柏拉图主义"),
    (W, R, "古典哲学的复兴", "亚里士多德主义"),
    (W, R, "宗教改革"),
    (W, R, "自然哲学与科学革命"),
    (W, E),
    (W, E, "唯理论"),
    (W, E, "唯理论", "唯理论总论"),
    (W, E, "唯理论", "笛卡尔与笛卡尔学派"),
    (W, E, "唯理论", "斯宾诺莎"),
    (W, E, "唯理论", "莱布尼茨-沃尔夫学派"),
    (W, E, "唯理论", "剑桥柏拉图学派"),
    (W, E, "经验论"),
    (W, E, "经验论", "培根与霍布斯"),
    (W, E, "经验论", "洛克"),
    (W, E, "经验论", "贝克莱"),
    (W, E, "经验论", "休谟"),
    (W, E, "经验论", "苏格兰常识学派"),
    (W, E, "经验论", "英国道德哲学与宗教哲学"),
    (W, E, "启蒙运动"),
    (W, E, "启蒙运动", "法国启蒙"),
    (W, E, "启蒙运动", "苏格兰启蒙"),
    (W, E, "启蒙运动", "德国启蒙"),
    (W, E, "启蒙运动", "自然法与社会契约"),
    (W, E, "德国古典哲学"),
    (W, E, "德国古典哲学", "康德"),
    (W, E, "德国古典哲学", "费希特"),
    (W, E, "德国古典哲学", "谢林"),
    (W, E, "德国古典哲学", "黑格尔"),
    (W, E, "浪漫主义与人文科学"),
    (W, N),
    (W, N, "后黑格尔与马克思主义"),
    (W, N, "后黑格尔与马克思主义", "青年黑格尔派"),
    (W, N, "后黑格尔与马克思主义", "马克思与恩格斯"),
    (W, N, "后黑格尔与马克思主义", "西方马克思主义"),
    (W, N, "非理性主义与生存哲学"),
    (W, N, "非理性主义与生存哲学", "叔本华"),
    (W, N, "非理性主义与生存哲学", "克尔凯郭尔"),
    (W, N, "非理性主义与生存哲学", "尼采"),
    (W, N, "实证主义与科学主义"),
    (W, N, "实证主义与科学主义", "第一代实证主义"),
    (W, N, "实证主义与科学主义", "马赫主义"),
    (W, N, "实证主义与科学主义", "维也纳学派与逻辑实证主义"),
    (W, N, "功利主义与古典自由主义"),
    (W, N, "新康德主义"),
    (W, N, "英国唯心论与实在论"),
    (W, N, "现象学运动"),
    (W, N, "存在主义与解释学"),
    (W, N, "分析哲学"),
    (W, N, "分析哲学", "早期分析哲学"),
    (W, N, "分析哲学", "日常语言哲学"),
    (W, N, "分析哲学", "分析形而上学"),
    (W, N, "分析哲学", "分析语言哲学"),
    (W, N, "分析哲学", "分析伦理学与政治哲学"),
    (W, N, "批判理论与法兰克福学派"),
    (W, N, "批判理论与法兰克福学派", "法兰克福学派"),
    (W, N, "批判理论与法兰克福学派", "批判理论专题"),
    (W, N, "结构主义与后结构主义"),
    (W, N, "结构主义与后结构主义", "结构主义与符号学"),
    (W, N, "结构主义与后结构主义", "后结构主义与解构"),
    (W, N, "实用主义与过程哲学"),
    (W, N, "现代政治哲学"),
    (W, N, "现代法哲学"),
    (W, J),
    (W, J, "古代与中世纪犹太哲学"),
    (W, J, "近代犹太哲学"),
    (W, J, "现代犹太哲学"),
    ("欧美以外哲学史",),
    ("欧美以外哲学史", "中国哲学"),
    ("欧美以外哲学史", "中国哲学", "先秦"),
    ("欧美以外哲学史", "中国哲学", "汉唐"),
    ("欧美以外哲学史", "中国哲学", "宋明"),
    ("欧美以外哲学史", "中国哲学", "清代"),
    ("欧美以外哲学史", "中国哲学", "现代"),
    ("欧美以外哲学史", "中国哲学", "中国佛教"),
    ("欧美以外哲学史", "中国哲学", "藏传佛教"),
    ("欧美以外哲学史", "中国哲学", "道教"),
    ("欧美以外哲学史", "中国哲学", "专题"),
    ("欧美以外哲学史", "印度哲学"),
    ("欧美以外哲学史", "印度哲学", "佛教"),
    ("欧美以外哲学史", "印度哲学", "耆那教"),
    ("欧美以外哲学史", "印度哲学", "正理-胜论"),
    ("欧美以外哲学史", "印度哲学", "弥曼差"),
    ("欧美以外哲学史", "印度哲学", "不二吠檀多"),
    ("欧美以外哲学史", "印度哲学", "早期现代"),
    ("欧美以外哲学史", "印度哲学", "专题"),
    ("欧美以外哲学史", "日本哲学"),
    ("欧美以外哲学史", "日本哲学", "古代与中世"),
    ("欧美以外哲学史", "日本哲学", "近世"),
    ("欧美以外哲学史", "日本哲学", "近代"),
    ("欧美以外哲学史", "日本哲学", "专题"),
    ("欧美以外哲学史", "韩国哲学"),
    ("欧美以外哲学史", "韩国哲学", "儒学"),
    ("欧美以外哲学史", "韩国哲学", "佛教"),
    ("欧美以外哲学史", "韩国哲学", "通论"),
    ("欧美以外哲学史", "伊斯兰哲学"),
    ("欧美以外哲学史", "伊斯兰哲学", "早期"),
    ("欧美以外哲学史", "伊斯兰哲学", "黄金时代"),
    ("欧美以外哲学史", "伊斯兰哲学", "后期"),
    ("欧美以外哲学史", "伊斯兰哲学", "专题"),
    ("欧美以外哲学史", "非洲与非裔哲学"),
    ("欧美以外哲学史", "非洲与非裔哲学", "传统非洲哲学"),
    ("欧美以外哲学史", "非洲与非裔哲学", "非裔哲学"),
    ("欧美以外哲学史", "非洲与非裔哲学", "当代"),
    ("欧美以外哲学史", "拉丁美洲哲学"),
    ("欧美以外哲学史", "拉丁美洲哲学", "19–20世纪"),
    ("欧美以外哲学史", "拉丁美洲哲学", "专题"),
    ("科学哲学",),
    ("科学哲学", "科学哲学史与学派"),
    ("科学哲学", "一般科学哲学"),
    ("科学哲学", "一般科学哲学", "科学方法与推理"),
    ("科学哲学", "一般科学哲学", "科学解释"),
    ("科学哲学", "一般科学哲学", "科学实在论与反实在论"),
    ("科学哲学", "一般科学哲学", "科学理论与模型"),
    ("科学哲学", "一般科学哲学", "科学实验与测量"),
    ("科学哲学", "一般科学哲学", "科学进步与革命"),
    ("科学哲学", "一般科学哲学", "科学的社会维度"),
    ("科学哲学", "物理学哲学"),
    ("科学哲学", "化学哲学"),
    ("科学哲学", "数学哲学"),
    ("科学哲学", "生物学哲学"),
    ("科学哲学", "医学哲学"),
    ("科学哲学", "认知科学与神经科学哲学"),
    ("科学哲学", "信息与计算科学哲学"),
    ("科学哲学", "社会科学哲学"),
    ("科学哲学", "技术哲学"),
    ("哲学通论",),
    ("哲学通论", "形而上学"),
    ("哲学通论", "形而上学", "本体论"),
    ("哲学通论", "形而上学", "模态与可能世界"),
    ("哲学通论", "形而上学", "同一性与变化"),
    ("哲学通论", "形而上学", "时间与空间哲学"),
    ("哲学通论", "形而上学", "因果关系"),
    ("哲学通论", "形而上学", "自由意志"),
    ("哲学通论", "形而上学", "哲学中的神秘传统"),
    ("哲学通论", "认识论"),
    ("哲学通论", "认识论", "元认识论"),
    ("哲学通论", "认识论", "知识论"),
    ("哲学通论", "认识论", "信念与证成"),
    ("哲学通论", "认识论", "社会认识论"),
    ("哲学通论", "认识论", "怀疑论"),
    ("哲学通论", "认识论", "证据与合理性"),
    ("哲学通论", "语言哲学与逻辑学"),
    ("哲学通论", "语言哲学与逻辑学", "语言哲学"),
    ("哲学通论", "语言哲学与逻辑学", "语义学"),
    ("哲学通论", "语言哲学与逻辑学", "语用学"),
    ("哲学通论", "语言哲学与逻辑学", "逻辑史与逻辑学家"),
    ("哲学通论", "语言哲学与逻辑学", "经典逻辑与传统逻辑"),
    ("哲学通论", "语言哲学与逻辑学", "非经典逻辑"),
    ("哲学通论", "语言哲学与逻辑学", "悖论与非形式逻辑"),
    ("哲学通论", "心灵哲学"),
    ("哲学通论", "心灵哲学", "心理现象与认知科学"),
    ("哲学通论", "心灵哲学", "他心问题"),
    ("哲学通论", "心灵哲学", "心灵因果性"),
    ("哲学通论", "心灵哲学", "意识"),
    ("哲学通论", "心灵哲学", "知觉"),
    ("哲学通论", "心灵哲学", "物理主义与二元论"),
    ("哲学通论", "心灵哲学", "延展心灵与外在主义"),
    ("哲学通论", "心灵哲学", "情感"),
    ("哲学通论", "伦理学"),
    ("哲学通论", "伦理学", "元伦理学"),
    ("哲学通论", "伦理学", "规范伦理学"),
    ("哲学通论", "伦理学", "价值论"),
    ("哲学通论", "伦理学", "道德心理学"),
    ("哲学通论", "伦理学", "行动哲学与理由论"),
    ("哲学通论", "伦理学", "社会伦理学"),
    ("哲学通论", "伦理学", "应用伦理学"),
    ("哲学通论", "政治哲学"),
    ("哲学通论", "政治哲学", "政治理论"),
    ("哲学通论", "政治哲学", "正义理论"),
    ("哲学通论", "政治哲学", "民主理论"),
    ("哲学通论", "政治哲学", "自由主义与共和主义"),
    ("哲学通论", "政治哲学", "全球正义与移民"),
    ("哲学通论", "政治哲学", "种族哲学"),
    ("哲学通论", "政治哲学", "政治义务与合法性"),
    ("哲学通论", "政治哲学", "社会理论与公共哲学"),
    ("哲学通论", "法哲学"),
    ("哲学通论", "宗教哲学"),
    ("哲学通论", "宗教哲学", "宗教哲学总论"),
    ("哲学通论", "宗教哲学", "上帝存在的论证"),
    ("哲学通论", "宗教哲学", "神学与教义"),
    ("哲学通论", "宗教哲学", "基督教神学"),
    ("哲学通论", "宗教哲学", "宗教与科学"),
    ("哲学通论", "环境哲学"),
    ("哲学通论", "美学"),
    ("哲学通论", "美学", "艺术哲学"),
    ("哲学通论", "女性主义哲学"),
    ("哲学通论", "女性主义哲学", "女性主义理论"),
    ("哲学通论", "女性主义哲学", "性别与酷儿哲学"),
    ("哲学通论", "女性主义哲学", "性哲学"),
    ("哲学通论", "教育哲学"),
    ("哲学通论", "经济哲学"),
    ("哲学通论", "经济哲学", "经济学家"),
    ("哲学通论", "决策与博弈论"),
    ("哲学通论", "文化哲学"),
    ("哲学通论", "出生与死亡哲学"),
]

# ---------------------------------------------------------------- 路径常量

def P(*parts: str) -> tuple[str, ...]:
    return tuple(parts)

MED = (W, M)
SCH = MED + ("经院哲学的兴盛",)
SPL = MED + ("经院哲学的分裂",)
LATE = MED + ("中世纪晚期",)
MOD = (W, N)
ANA = MOD + ("分析哲学",)
CRI = MOD + ("批判理论与法兰克福学派",)
STR = MOD + ("结构主义与后结构主义",)
EMP = (W, E, "经验论")
SP = ("科学哲学",)
SPH = SP + ("科学哲学史与学派",)
GEN = SP + ("一般科学哲学",)
PHYS = SP + ("物理学哲学",)
MATH = SP + ("数学哲学",)
BIO = SP + ("生物学哲学",)
MEDP = SP + ("医学哲学",)
COG = SP + ("认知科学与神经科学哲学",)
INFO = SP + ("信息与计算科学哲学",)
SOC = SP + ("社会科学哲学",)
TECH = SP + ("技术哲学",)
PHIL = ("哲学通论",)
META = PHIL + ("形而上学",)
EPIS = PHIL + ("认识论",)
LANG = PHIL + ("语言哲学与逻辑学",)
MIND = PHIL + ("心灵哲学",)
ETH = PHIL + ("伦理学",)
POL = PHIL + ("政治哲学",)
REL = PHIL + ("宗教哲学",)
AES = PHIL + ("美学",)
FEM = PHIL + ("女性主义哲学",)

# ---------------------------------------------------------------- 节级映射（改名/拆分/合并）

SECTION_MAP: dict[tuple[str, ...], tuple[str, ...]] = {
    # 古代
    (W, A, "晚期希腊与罗马哲学"): (W, A, "希腊化与罗马哲学"),
    # 中世纪
    (W, M, "思想来源与教父哲学", "奥古斯丁"): MED + ("思想来源与教父哲学", "拉丁教父与奥古斯丁"),
    (W, M, "经院哲学的诞生", "安瑟伦与早期经院"): MED + ("经院哲学的诞生", "安瑟伦与理性主义神学"),
    (W, M, "经院哲学的诞生", "阿伯拉尔与12世纪"): MED + ("经院哲学的诞生", "阿伯拉尔与共相之争"),
    (W, M, "经院哲学的兴盛", "大阿尔伯特与阿奎那"): SCH + ("大阿尔伯特与托马斯主义",),
    (W, M, "经院哲学的分裂", "1277年谴责"): SPL + ("1277 年谴责",),
    (W, M, "经院哲学的分裂", "奥康主义与“现代路线”"): SPL + ("唯名论与现代路线",),
    # 现代
    (W, N, "批判理论"): CRI,
    (W, N, "结构主义与后结构主义"): STR,
    (W, N, "新康德主义与英国唯心论"): MOD + ("新康德主义",),
    (W, N, "分析哲学", "后实证科学哲学"): SPH,
    (W, N, "分析哲学", "分析形而上学与语言哲学"): ANA + ("分析形而上学",),
    (W, N, "政治哲学与法哲学"): MOD + ("现代政治哲学",),
    # 哲学通论
    (PHIL, "心理学与心灵哲学"): MIND,
    (PHIL, "心理学与心灵哲学", "他心问题（关于他心的怀疑论问题、动物心灵，人工智能心灵与意识）"): MIND + ("他心问题",),
    (PHIL, "心理学与心灵哲学", "心灵因果性（因果排他性、非还原论物理主义）"): MIND + ("心灵因果性",),
    (PHIL, "心理学与心灵哲学", "心灵的特征（心灵的私人性，意向性，民间心理学）"): MIND + ("心理现象与认知科学",),
    (PHIL, "心理学与心灵哲学", "物理主义"): MIND + ("物理主义与二元论",),
    (PHIL, "心理学与心灵哲学", "知觉"): MIND + ("知觉",),
    (PHIL, "心理学与心灵哲学", "关于意识的形而上学问题（二元论与罗素一元论、幻象论）"): MIND + ("意识",),
    (PHIL, "心理学与心灵哲学", "外在主义与延展心灵"): MIND + ("延展心灵与外在主义",),
    (PHIL, "心理学与心灵哲学", "意识研究"): MIND + ("意识",),
    (PHIL, "心理学与心灵哲学", "认知科学"): MIND + ("心理现象与认知科学",),
    (PHIL, "心理学与心灵哲学", "情感哲学"): MIND + ("情感",),
    (PHIL, "语言哲学与逻辑学", "逻辑学家"): LANG + ("逻辑史与逻辑学家",),
    (PHIL, "语言哲学与逻辑学", "逻辑史"): LANG + ("逻辑史与逻辑学家",),
    (PHIL, "语言哲学与逻辑学", "非经典逻辑（哲学逻辑、现代逻辑、高阶逻辑）"): LANG + ("非经典逻辑",),
    (PHIL, "语言哲学与逻辑学", "经典逻辑（标准逻辑）与传统逻辑"): LANG + ("经典逻辑与传统逻辑",),
    (PHIL, "语言哲学与逻辑学", "形式逻辑与非形式逻辑（批判性思维、辩证逻辑即辩证法、悖论）"): LANG + ("悖论与非形式逻辑",),
    (PHIL, "认识论", "认识论正当性"): EPIS + ("信念与证成",),
    (PHIL, "认识论", "合理性"): EPIS + ("证据与合理性",),
    (PHIL, "认识论", "证据"): EPIS + ("证据与合理性",),
    (PHIL, "伦理学（道德哲学）"): ETH,
    (PHIL, "伦理学（道德哲学）", "价值观哲学（价值论、好生活、道德情感与德性）"): ETH + ("价值论",),
    (PHIL, "伦理学（道德哲学）", "规范伦理学(后果主义、西方古典伦理学、功利论、义务论、契约论和德性论)"): ETH + ("规范伦理学",),
    (PHIL, "伦理学（道德哲学）", "社会伦理学（家庭伦理（家庭婚姻）、人际伦理（友谊）、环境伦理）"): ETH + ("社会伦理学",),
    (PHIL, "伦理学（道德哲学）", "社会正义（结构性不平等和不公正、对待他人的平等和尊重）"): POL + ("正义理论",),
    (PHIL, "伦理学（道德哲学）", "人权（个体的基本权利和自由）"): POL + ("政治理论",),
    (PHIL, "政治哲学", "政治家"): POL + ("正义理论",),
    (PHIL, "政治哲学", "全球化和移民哲学"): POL + ("全球正义与移民",),
    (PHIL, "政治哲学", "社会理论和公共哲学（公共政策、公共事务）"): POL + ("社会理论与公共哲学",),
    (PHIL, "神学与宗教哲学"): REL,
    (PHIL, "神学与宗教哲学", "神学（教义通论）"): REL + ("神学与教义",),
    (PHIL, "神学与宗教哲学", "基督教"): REL + ("基督教神学",),
    (PHIL, "神学与宗教哲学", "上帝存在的论证"): REL + ("上帝存在的论证",),
    (PHIL, "神学与宗教哲学", "宗教哲学与宗教学通论"): REL + ("宗教哲学总论",),
    (PHIL, "女性哲学与性哲学相关"): FEM,
    (PHIL, "女性哲学与性哲学相关", "女性主义哲学"): FEM + ("女性主义理论",),
    (PHIL, "女性哲学与性哲学相关", "性哲学（性伦理学、性与道德和权力）"): FEM + ("性哲学",),
    (PHIL, "女性哲学与性哲学相关", "性别与酷儿哲学（关于性别身份、角色、酷儿理论、多样化的性别和性取向）"): FEM + ("性别与酷儿哲学",),
    (PHIL, "社会学哲学"): SOC,
    (PHIL, "科学哲学"): SP,
    (PHIL, "科学哲学", "科学家"): SPH,
    (PHIL, "科学哲学", "科学方法论与科学知识论"): GEN + ("科学方法与推理",),
    (PHIL, "科学哲学", "科学实在论(理论解释力、理论变化、理论结构、现实的真实性、概念的实在性)"): GEN + ("科学实在论与反实在论",),
    (PHIL, "科学哲学", "科学认识论"): GEN + ("科学方法与推理",),
    (PHIL, "科学哲学", "混沌理论"): PHYS,
    (PHIL, "科学哲学", "认知神经哲学"): COG,
    (PHIL, "科学哲学", "信息和数字文化哲学（信息哲学、伦理学相关）"): INFO,
    (PHIL, "科学哲学", "物理学哲学"): PHYS,
    (PHIL, "科学哲学", "数学哲学"): MATH,
    (PHIL, "科学哲学", "化学哲学"): SP + ("化学哲学",),
    (PHIL, "科学哲学", "生命科学哲学（生物学、生态学、遗传学）"): BIO,
    (PHIL, "科学哲学", "医学人文学和医学哲学（医学本质，健康疾病定义，医学伦理）"): MEDP,
    (PHIL, "科学哲学", "技术哲学"): TECH,
    (PHIL, "博弈论"): PHIL + ("决策与博弈论",),
    (PHIL, "决策理论"): PHIL + ("决策与博弈论",),
    (PHIL, "出生哲学与死亡哲学"): PHIL + ("出生与死亡哲学",),
    # 欧美以外：叶子同名直接命中，无需登记
}

ABE = MED + ("经院哲学的诞生", "阿伯拉尔与共相之争")
LOG12 = MED + ("经院哲学的诞生", "12 世纪人文与逻辑学派")
THOM = SCH + ("大阿尔伯特与托马斯主义",)
FRAN = SCH + ("波纳文图拉与方济各传统",)
AUGU = SCH + ("奥古斯丁主义复兴",)
SCHL = SCH + ("经院哲学的逻辑与自然哲学",)
NOM = SPL + ("唯名论与现代路线",)
MYST = LATE + ("德意志神秘主义",)
MODTOP = MED + ("中世纪哲学专题",)
MPOL = MOD + ("现代政治哲学",)
PRAG = MOD + ("实用主义与过程哲学",)
PHEN = MOD + ("现象学运动",)
EXIS = MOD + ("存在主义与解释学",)
UKI = MOD + ("英国唯心论与实在论",)
NK = MOD + ("新康德主义",)
POSI = MOD + ("实证主义与科学主义", "第一代实证主义")
FEMT = FEM + ("女性主义理论",)
FEMG = FEM + ("性别与酷儿哲学",)
FEMS = FEM + ("性哲学",)
LANGP = LANG + ("语言哲学",)
LOGH = LANG + ("逻辑史与逻辑学家",)
NCL = LANG + ("非经典逻辑",)
ACTION = ETH + ("行动哲学与理由论",)
NORM = ETH + ("规范伦理学",)
VAL = ETH + ("价值论",)
JUST = POL + ("正义理论",)
PTHEORY = POL + ("政治理论",)
ARTH = AES + ("艺术哲学",)
SCM = GEN + ("科学方法与推理",)
SCE = GEN + ("科学解释",)
SCR = GEN + ("科学实在论与反实在论",)
STM = GEN + ("科学理论与模型",)
SEX = GEN + ("科学实验与测量",)
SPR = GEN + ("科学进步与革命",)
SSO = GEN + ("科学的社会维度",)
CAUS = META + ("因果关系",)
IDENT = META + ("同一性与变化",)
LAWP = PHIL + ("法哲学",)
EDU = PHIL + ("教育哲学",)

# ---------------------------------------------------------------- 条目级调整（slug 路径 → 新节）

ITEM_MAP: dict[str, tuple[str, ...]] = {
    # —— 中世纪：经院哲学兴盛期的学派细分
    "p/philip-chancellor.md": SCHL, "g/grosseteste.md": SCHL, "l/llull.md": SCHL,
    "e/erfurt.md": SCHL, "s/simon-faversham.md": SCHL, "r/radulphus-brito.md": SCHL,
    "s/sharpe.md": SCHL, "a/alyngton.md": SCHL, "p/penbygull.md": SCHL,
    "p/paul-venice.md": SCHL, "b/burley.md": SCHL,
    "h/henry-ghent.md": AUGU, "w/william-auvergne.md": AUGU,
    "b/bonaventure.md": FRAN, "o/olivi.md": FRAN, "r/roger-bacon.md": FRAN,
    "g/giles.md": THOM,
    "a/auriol.md": NOM, "h/holkot.md": NOM, "a/autrecourt.md": NOM,
    "m/meister-eckhart.md": MYST, "d/dietrich-freiberg.md": MYST,
    "m/medieval-political.md": MODTOP, "m/marsilius-padua.md": MODTOP,
    "u/universals-medieval.md": ABE,
    "l/lambert-auxerre.md": LOG12, "w/william-sherwood.md": LOG12,
    "r/richard-sophister.md": LOG12, "p/peter-spain.md": LOG12,
    "j/john-salisbury.md": LOG12,
    # —— 现代哲学：新康德主义与英国唯心论节的溢出条目
    "p/process-philosophy.md": PRAG, "w/whitehead.md": PRAG, "h/hartshorne.md": PRAG,
    "p/process-theism.md": REL + ("神学与教义",),
    "m/mary-shepherd.md": EMP + ("英国道德哲学与宗教哲学",),
    "s/scottish-19th.md": EMP + ("苏格兰常识学派",),
    "f/fechner.md": MIND + ("心理现象与认知科学",),
    "w/wilhelm-wundt.md": MIND + ("心理现象与认知科学",),
    "h/hermann-helmholtz.md": COG,
    "g/george-eliot.md": POSI,
    "d/dilthey.md": EXIS,
    "j/james-ward.md": UKI, "a/anderson-john.md": UKI,
    "c/collingwood.md": UKI, "c/collingwood-aesthetics.md": UKI,
    "c/croce-aesthetics.md": ARTH,
    "m/montessori-maria.md": EDU, "j/johann-herbart.md": EDU,
    "w/well-being.md": VAL, "f/findlay.md": ANA + ("分析形而上学",),
    "b/bradley.md": UKI, "b/bradley-moral.md": UKI, "b/bradley-regress.md": UKI,
    "b/bosanquet.md": UKI, "m/mctaggart.md": UKI, "a/alexander.md": UKI,
    # —— 批判理论与法兰克福学派
    "c/critical-theory.md": CRI + ("法兰克福学派",),
    "b/benjamin.md": CRI + ("法兰克福学派",),
    "h/horkheimer.md": CRI + ("法兰克福学派",),
    "m/marcuse.md": CRI + ("法兰克福学派",),
    "a/adorno.md": CRI + ("法兰克福学派",),
    "h/habermas.md": CRI + ("法兰克福学派",),
    # —— 结构主义与后结构主义
    "l/lacan.md": STR + ("结构主义与符号学",),
    "p/postmodernism.md": STR + ("后结构主义与解构",),
    "l/lyotard.md": STR + ("后结构主义与解构",),
    "d/deleuze.md": STR + ("后结构主义与解构",),
    "f/foucault.md": STR + ("后结构主义与解构",),
    "b/baudrillard.md": STR + ("后结构主义与解构",),
    "d/derrida.md": STR + ("后结构主义与解构",),
    # —— 现代政治哲学
    "s/socialism.md": PTHEORY, "c/capitalism.md": PTHEORY,
    "r/rationality-instrumental.md": ACTION,
    # —— 分析哲学节：逻辑学家迁回逻辑学
    "b/boole.md": LOGH, "b/bolzano.md": LOGH, "b/brouwer.md": LOGH,
    "g/goedel.md": LOGH, "m/mally.md": LOGH, "s/scholz.md": LOGH,
    "p/prior.md": LOGH, "c/church.md": LOGH, "t/tarski.md": LOGH,
    "l/lesniewski.md": LOGH, "l/lvov-warsaw.md": LOGH, "l/lukasiewicz.md": LOGH,
    # —— 分析哲学节：现象学、行动哲学、规范伦理学的散件
    "m/marty.md": PHEN,
    "a/agency.md": ACTION, "s/shared-agency.md": ACTION,
    "c/consequentializing.md": NORM,
    # —— 分析哲学节：美学与数学哲学
    "l/langer.md": ARTH, "b/beardsley-aesthetics.md": ARTH,
    "g/goodman-aesthetics.md": ARTH, "w/weyl.md": MATH,
    "a/aesthetic-concept.md": AES,
    # —— 分析语言哲学
    "l/linguistics.md": LANGP,
    "q/quine.md": ANA + ("分析语言哲学",), "q/quine-nf.md": ANA + ("分析语言哲学",),
    "s/sellars.md": ANA + ("分析语言哲学",), "d/davidson.md": ANA + ("分析语言哲学",),
    "w/williams-bernard.md": ANA + ("分析语言哲学",),
    "s/sylvan-routley.md": ANA + ("分析语言哲学",), "g/goodman.md": ANA + ("分析语言哲学",),
    # —— 女性主义：从分析哲学节收拢
    "f/feminist-philosophy.md": FEMT,
    "f/femapproach-analytic.md": FEMT, "f/femapproach-analy-cont.md": FEMT,
    "f/femapproach-pragmatism.md": FEMT, "f/femapproach-prag-cont.md": FEMT,
    "f/femapproach-continental.md": FEMT, "f/feminism-femhist.md": FEMT,
    "f/feminism-epistemology.md": FEMT, "f/feminist-social-epistemology.md": FEMT,
    "f/feminism-metaphysics.md": FEMT, "f/feminism-argumentation.md": FEMT,
    "f/feminist-science.md": FEMT, "f/feminist-philosophy-biology.md": FEMT,
    "f/feminism-environmental.md": FEMT, "f/feminism-aesthetics.md": FEMT,
    "f/feminism-language.md": FEMT, "f/feminism-law.md": FEMT,
    "f/feminism-political.md": FEMT, "f/feminism-ethics.md": FEMT,
    "f/feminism-moralpsych.md": FEMT, "f/feminist-bioethics.md": FEMT,
    "f/feminism-disability.md": FEMT, "f/feminism-family.md": FEMT,
    "f/feminist-religion.md": FEMT, "f/feminism-globalization.md": FEMT,
    "h/histfem-condorcet.md": FEMT,
    "f/feminism-gender.md": FEMG, "f/feminism-trans.md": FEMG,
    "f/feminist-body.md": FEMG, "f/feminism-self.md": FEMG,
    "f/feminism-autonomy.md": FEMG, "f/feminism-objectification.md": FEMG,
    "f/feminist-power.md": FEMG, "f/feminism-class.md": FEMG,
    "f/feminist-sex-markets.md": FEMS, "p/pornography-censorship.md": FEMS,
    "f/feminism-rape.md": FEMS,
    "t/trans.md": FEMG,
}

# ---------------------------------------------------------------- 解析与生成

HEAD = re.compile(r"^(\#{1,4})\s+(.*)$")
ITEM = re.compile(r"^(\s*)\*\s+\[(.*)\]\(([^)]+)\)\s*$")


def strip_tail_paren(t: str) -> str:
    """去掉末尾成对的括注（支持嵌套）。"""
    while t and t[-1] in "）)":
        close = t[-1]
        open_ = "（" if close == "）" else "("
        depth = 0
        for i in range(len(t) - 1, -1, -1):
            if t[i] == close:
                depth += 1
            elif t[i] == open_:
                depth -= 1
                if depth == 0:
                    t = t[:i].rstrip()
                    break
        else:
            break
    return t


def clean(t: str) -> str:
    t = t.strip()
    t = re.sub(r"^[一二三四五六七八九十]+、\s*", "", t)
    t = re.sub(r"^\d+(\.\d+)*\s+", "", t)
    t = strip_tail_paren(t)
    return re.sub(r"\s+", " ", t).strip()


DEINDENT = {
    # 原文件中语义并列却误排为子条目的条目：统一提升为同级
    "s/scientific-knowledge-social.md", "e/experimental-philosophy.md", "t/thought-experiment.md",
    "a/atomism-modern.md", "s/statphys-Boltzmann.md", "f/fine-tuning.md",
    "a/algebra.md", "i/infinity.md",
    "c/creationism.md", "s/sociobiology.md", "d/decision-capacity.md",
    "n/nicolai-hartmann.md", "d/determinate-determinables.md", "o/ontological-commitment.md",
    "f/facts.md", "t/tropes.md", "e/events.md",
    "p/possibilism-actualism.md", "c/change.md", "a/animalism.md", "s/spacetime-bebecome.md",
    "g/games-abstraction.md", "l/lesniewski.md", "w/wittgenstein.md",
    "w/wittgenstein-atomism.md", "w/wittgenstein-mathematics.md", "w/wittgenstein-aesthetics.md",
    "b/bolzano-logic.md", "l/lambda-calculus.md",
    "l/logic-action.md", "l/logic-power-games.md", "l/logics-for-games.md", "l/logic-games.md",
    "t/type-theory-intuitionistic.md",
    "r/reasoning-analogy.md", "a/argument.md", "p/paradox-skolem.md", "f/fallacies.md",
    "i/intentionality.md", "c/collective-intentionality.md", "p/phenomenal-intentionality.md",
    "c/content-causal.md", "c/content-narrow.md", "c/content-nonconceptual.md",
    "c/content-teleological.md", "m/mental-representation.md",
    "a/action-perception.md", "s/simplicity.md",
    "l/language-thought.md", "i/inner-speech.md", "i/innateness-language.md", "c/concepts.md",
    "d/dualism.md", "p/panpsychism.md", "n/neutral-monism.md", "p/pain.md",
    "a/action-based-perception.md", "s/sense-data.md", "m/molyneux-problem.md", "c/color.md",
    "p/physicalism.md", "m/multiple-realizability.md", "b/behaviorism.md",
    "e/externalism-self-knowledge.md", "e/emotion.md", "e/empathy.md",
    "m/moral-epistemology.md", "m/moral-epistemology-a-priori.md", "e/egoism.md",
    "e/experimental-moral.md", "t/terrorism.md", "e/ethics-business.md", "i/intellectual-property.md",
    "i/identity-politics.md", "n/nationalism.md", "r/reflective-equilibrium.md",
    "c/capability-approach.md", "j/jury-theorems.md",
    "j/justification-public.md", "d/dirty-hands.md", "r/revolution.md", "s/secession.md",
    "s/solidarity.md", "g/god-ultimates.md", "g/god-necessary-being.md",
    "f/feminism-moralpsych.md", "f/feminism-ethics.md", "f/feminist-bioethics.md",
    "h/histfem-condorcet.md", "h/heinrich-rickert.md", "v/vaihinger.md", "p/personalism.md",
    "y/yorck.md", "a/authenticity.md", "m/merleau-ponty.md", "r/robert-kilwardby.md",
    "w/walter-chatton.md", "f/francis-marchia.md", "c/crathorn.md", "g/gregory-rimini.md",
    "d/du-bos.md", "p/persons-means.md",
}


def parse():
    lines = SRC.read_text(encoding="utf-8").splitlines()
    heads = [""] * 4
    units: list[dict] = []
    notes: dict[tuple[str, ...], list[str]] = {}
    cur = None
    for line in lines:
        m = HEAD.match(line)
        if m:
            lvl = len(m.group(1))
            heads = heads[: lvl - 1] + [m.group(2).strip()] + [""] * (4 - lvl)
            cur = None
            continue
        m = ITEM.match(line)
        if m:
            indent = len(m.group(1))
            path = m.group(3)
            sec = tuple(clean(x) for x in heads if x)
            if path in DEINDENT:
                indent = 0
            if indent == 0 or cur is None:
                cur = {"lines": [line.strip()], "path": path, "sec": sec, "children": []}
                units.append(cur)
            else:
                cur["children"].append({"lines": [line.strip()], "path": path, "sec": sec})
            continue
        if line.startswith(">"):
            sec = tuple(clean(x) for x in heads if x)
            notes.setdefault(sec, []).append(line.rstrip())
            cur = None
    return units, notes


def flatten_key(key: tuple) -> tuple[str, ...]:
    out: list[str] = []
    for x in key:
        if isinstance(x, tuple):
            out.extend(flatten_key(x))
        else:
            out.append(clean(x))
    return tuple(out)


CLEAN_SECTION_MAP: dict[tuple[str, ...], tuple[str, ...]] = {
    flatten_key(k): v for k, v in SECTION_MAP.items()
}

H2_ALIAS = {"中古哲学": "中世纪哲学"}
LEAF_ALIAS = {"模态实在论": "模态与可能世界", "身份与变化": "同一性与变化"}


def section_target(sec: tuple[str, ...]) -> tuple[str, ...] | None:
    labels = [clean(x) for x in sec]
    for i, lab in enumerate(labels):
        labels[i] = H2_ALIAS.get(lab, lab)
    labels[-1] = LEAF_ALIAS.get(labels[-1], labels[-1])
    key = tuple(labels)
    if key in CLEAN_SECTION_MAP:
        return CLEAN_SECTION_MAP[key]
    for n in (2, 1):
        tail = tuple(labels[-n:])
        hits = [p for p in NODE_SET if tuple(p[-n:]) == tail]
        if len(hits) == 1:
            return hits[0]
    return None


def main() -> int:
    units, notes = parse()
    header = SRC.read_text(encoding="utf-8").splitlines()[:4]

    buckets: dict[tuple[str, ...], list[dict]] = {p: [] for p in SKELETON}
    unresolved: list[tuple[tuple[str, ...], str]] = []

    for u in units:
        target = ITEM_MAP.get(u["path"]) or section_target(u["sec"])
        if target is None:
            unresolved.append((u["sec"], u["path"]))
            continue
        if target not in buckets:
            unresolved.append((("ITEM_MAP 目标不在骨架",) + target, u["path"]))
            continue
        # 子条目：目标节不同则脱钩为独立条目
        kept_children = []
        for c in u["children"]:
            ct = ITEM_MAP.get(c["path"]) or target
            if ct == target:
                kept_children.append(c)
            else:
                buckets.setdefault(ct, []).append({"lines": [x.lstrip() for x in c["lines"]],
                                                   "path": c["path"], "sec": c["sec"],
                                                   "children": []})
        buckets[target].append({"lines": u["lines"], "path": u["path"], "sec": u["sec"],
                                "children": kept_children})

    if unresolved:
        for sec, path in unresolved:
            print("UNRESOLVED", sec, path, file=sys.stderr)
        print(f"未解析 {len(unresolved)} 条，拒绝写回", file=sys.stderr)
        return 1

    # 注记
    note_map: dict[tuple[str, ...], list[str]] = {}
    for sec, lines in notes.items():
        t = section_target(sec)
        if t:
            note_map.setdefault(t, []).extend(lines)

    children = {p: [] for p in SKELETON}
    for p in SKELETON:
        if len(p) > 1:
            children[p[:-1]].append(p)

    def has(p: tuple[str, ...]) -> bool:
        return bool(buckets[p] or note_map.get(p) or any(has(c) for c in children[p]))

    out: list[str] = list(header) + [""]

    def emit(p: tuple[str, ...]) -> None:
        if not has(p):
            return
        out.append("#" * len(p) + " " + p[-1])
        out.append("")
        for line in note_map.get(p, []):
            out.append(line)
        if note_map.get(p):
            out.append("")
        for u in buckets[p]:
            out.extend(u["lines"])
            for c in u["children"]:
                out.extend("  " + x.lstrip() for x in c["lines"])
        if buckets[p]:
            out.append("")
        for c in children[p]:
            emit(c)

    for p in SKELETON:
        if len(p) == 1:
            emit(p)

    text = "\n".join(out).rstrip() + "\n"

    # 对账
    before = sorted(re.findall(r"\]\(([^)]+)\)", SRC.read_text(encoding="utf-8")))
    after = sorted(re.findall(r"\]\(([^)]+)\)", text))
    if before != after:
        print(f"链接不守恒：before={len(before)} after={len(after)}", file=sys.stderr)
        only_b = set(before) - set(after)
        only_a = set(after) - set(before)
        print("丢失", sorted(only_b)[:20], file=sys.stderr)
        print("多出", sorted(only_a)[:20], file=sys.stderr)
        return 1

    OUT.write_text(text, encoding="utf-8")
    print(f"写入 {OUT}；条目 {len(before)} 条；节 {sum(1 for p in SKELETON if has(p))} 个")
    return 0


NODE_SET = set(SKELETON)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from items import EXTRA  # noqa: E402

ITEM_MAP.update(EXTRA)

if __name__ == "__main__":
    sys.exit(main())

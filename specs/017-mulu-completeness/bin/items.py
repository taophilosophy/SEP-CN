# -*- coding: utf-8 -*-
"""条目级补充映射（第二批）：科学哲学、语言与逻辑、认识论、形而上学等。"""
W, A, M, R, E, N, J = "西方哲学史", "古代哲学", "中世纪哲学", "文艺复兴与宗教改革", "近代哲学", "现代哲学", "犹太哲学"
MED, SCH, SPL, LATE = (W, M), (W, M, "经院哲学的兴盛"), (W, M, "经院哲学的分裂"), (W, M, "中世纪晚期")
MOD, ANA, CRI, STR = (W, N), (W, N, "分析哲学"), (W, N, "批判理论与法兰克福学派"), (W, N, "结构主义与后结构主义")
EMP = (W, E, "经验论")
PHIL = ("哲学通论",)
SP = ("科学哲学",)
SPH, GEN = SP + ("科学哲学史与学派",), SP + ("一般科学哲学",)
PHYS, MATH = SP + ("物理学哲学",), SP + ("数学哲学",)
BIO, MEDP = SP + ("生物学哲学",), SP + ("医学哲学",)
COG, INFO = SP + ("认知科学与神经科学哲学",), SP + ("信息与计算科学哲学",)
SOC, TECH = SP + ("社会科学哲学",), SP + ("技术哲学",)
META, EPIS = PHIL + ("形而上学",), PHIL + ("认识论",)
LANG, MIND = PHIL + ("语言哲学与逻辑学",), PHIL + ("心灵哲学",)
ETH, POL = PHIL + ("伦理学",), PHIL + ("政治哲学",)
REL, AES, FEM = PHIL + ("宗教哲学",), PHIL + ("美学",), PHIL + ("女性主义哲学",)
LANGP, LOGH, NCL = LANG + ("语言哲学",), LANG + ("逻辑史与逻辑学家",), LANG + ("非经典逻辑",)
SCM, SCE, SCR = GEN + ("科学方法与推理",), GEN + ("科学解释",), GEN + ("科学实在论与反实在论",)
STM, SEX, SPR = GEN + ("科学理论与模型",), GEN + ("科学实验与测量",), GEN + ("科学进步与革命",)
SSO = GEN + ("科学的社会维度",)
CAUS, IDENT = META + ("因果关系",), META + ("同一性与变化",)
LAWP, ARTH = PHIL + ("法哲学",), AES + ("艺术哲学",)
PTHEORY = POL + ("政治理论",)

EXTRA = {
    # —— 科学哲学：科学家节
    "n/newton-stm.md": PHYS, "n/newton-philosophy.md": PHYS, "n/newton-principia.md": PHYS,
    "g/goedel-incompleteness.md": MATH, "c/church-turing.md": INFO,
    # —— 科学哲学：方法论节
    "c/comparative-cognition.md": COG, "c/constructive-empiricism.md": SCR,
    "h/holism-social.md": SOC, "a/agent-modeling-philscience.md": STM,
    "m/models-science.md": STM, "e/einstein-philscience.md": PHYS,
    "p/physics-experiment.md": SEX, "p/physics-structuralism.md": PHYS,
    "s/scientific-reduction.md": SCR, "s/scientific-pluralism.md": SCM,
    "s/science-big-data.md": SSO, "s/scientific-knowledge-social.md": SSO,
    "e/experimental-aesthetics.md": ARTH, "e/experimental-jurisprudence.md": LAWP,
    "s/simplicity.md": SCM, "d/divine-simplicity.md": REL + ("神学与教义",),
    "s/simulations-science.md": STM, "i/incommensurability.md": SPR,
    "l/laws-of-nature.md": STM, "c/ceteris-paribus.md": SCE,
    "c/causal-explanation-science.md": SCE, "s/scientific-explanation-20th.md": SCE,
    "m/measurement-science.md": SEX,
    # —— 科学哲学：实在论节
    "s/science-mechanisms.md": SCE, "p/physics-interrelate.md": PHYS,
    "p/prediction-accommodation.md": SCM, "r/rationality-historicist.md": SPR,
    "s/scientific-reproducibility.md": SSO, "s/scientific-discovery.md": SCM,
    "s/scientific-objectivity.md": SSO, "s/scientific-representation.md": STM,
    "s/structure-scientific-theories.md": STM,
    # —— 科学哲学：认识论节
    "c/confirmation.md": SCM, "e/epistemology-naturalized.md": EPIS + ("知识论",),
    "p/pseudo-science.md": SCM, "s/science-theory-observation.md": SCR,
    "s/scientific-unity.md": SPR, "s/scientific-underdetermination.md": SCR,
    # —— 科学哲学：混沌理论节
    "c/chaos.md": PHYS, "e/ergodic-hierarchy.md": PHYS,
    "c/causal-models.md": CAUS, "c/causation-mani.md": CAUS,
    "c/causation-regularity.md": CAUS, "c/consciousness-neuroscience.md": COG,
    # —— 科学哲学：认知神经哲学节
    "n/neuroscience.md": COG, "p/psychiatry.md": COG, "p/psychotherapy.md": COG,
    "e/ethics-ai.md": INFO, "a/algorithmic-fairness.md": INFO,
    "c/computing-responsibility.md": INFO, "e/ethics-internet-research.md": INFO,
    "e/ethics-search.md": INFO, "i/information.md": INFO,
    "i/information-biological.md": INFO, "o/ontology-is.md": INFO,
    "m/model-organisms.md": BIO, "i/information-semantic.md": INFO,
    "i/it-moral-values.md": INFO, "e/ethics-it-phenomenology.md": INFO,
    "i/it-privacy.md": INFO, "l/logic-information.md": INFO,
    # —— 科学哲学：信息与数字文化节中的物理学条目
    "c/causation-physics.md": PHYS, "c/computation-physicalsystems.md": PHYS,
    "e/equivME.md": PHYS, "s/statphys-statmech.md": PHYS,
    "i/information-entropy.md": PHYS, "g/genrel-early.md": PHYS,
    "s/spacetime-convensimul.md": PHYS, "s/spacetime-holearg.md": PHYS,
    "c/cosmology-30s.md": PHYS, "c/cosmology.md": PHYS,
    "c/cosmology-theology.md": REL + ("宗教与科学",),
    "c/cellular-automata.md": INFO,
    # —— 物理学哲学节中的数学条目
    "d/deductivism-mathematics.md": MATH, "m/mathematics-explanation.md": MATH,
    "m/mathematics-constructive.md": MATH, "m/mathematics-nondeductive.md": MATH,
    "a/algebra.md": MATH, "i/infinity.md": MATH,
    # —— 生命科学与医学
    "b/biomedicine.md": MEDP, "i/immunology.md": MEDP, "c/cancer.md": MEDP,
    "m/medicine.md": MEDP, "d/disability.md": MEDP, "h/health-disease.md": MEDP,
    "m/mental-disorder.md": MEDP, "i/informed-consent.md": MEDP,
    "a/advance-directives.md": MEDP, "d/disability-care-rationing.md": MEDP,
    "d/disability-well-being.md": MEDP, "j/justice-healthcareaccess.md": MEDP,
    "p/privacy-medicine.md": MEDP, "p/publichealth-ethics.md": MEDP,
    "e/enhancement.md": MEDP, "c/chimeras.md": MEDP, "c/cloning.md": MEDP,
    "s/stem-cells.md": MEDP, "t/theory-bioethics.md": MEDP, "a/abortion.md": MEDP,
    "c/clinical-research.md": MEDP, "g/gametes-donation-sale.md": MEDP,
    "o/organ-donation.md": MEDP, "n/neuroethics.md": MEDP, "o/organs-sale.md": MEDP,
    "d/decision-capacity.md": MEDP,
    # —— 语言哲学：从语义学节移出
    "s/states-of-affairs.md": LANGP, "r/rule-following.md": LANGP,
    "p/private-language.md": LANGP, "l/logical-form.md": LANGP, "a/analysis.md": LANGP,
    "f/fictionalism-modal.md": LANGP, "f/fictionalism.md": LANGP,
    "r/rigid-designators.md": LANGP, "p/propositions.md": LANGP,
    "p/propositions-singular.md": LANGP, "p/propositions-structured.md": LANGP,
    "g/generics.md": LANGP, "c/convention.md": LANGP,
    "t/truth-axiomatic.md": LANGP, "t/truth.md": LANGP,
    "t/truth-primitivist.md": LANGP, "t/truth-coherence.md": LANGP,
    "t/truth-correspondence.md": LANGP, "t/truth-deflationary.md": LANGP,
    "t/truth-identity.md": LANGP, "t/truth-pluralist.md": LANGP,
    "t/truth-pragmatic.md": LANGP, "t/truth-revision.md": LANGP,
    "t/truthlikeness.md": LANGP,
    # —— 语用学节中的逻辑条目
    "l/logic-paraconsistent.md": NCL, "l/logic-justification.md": NCL,
    "l/logic-many-sorted.md": NCL, "l/logic-manyvalued.md": NCL,
    "l/logic-nonmonotonic.md": NCL, "l/logic-relevance.md": NCL,
    "l/logic-substructural.md": NCL, "l/logic-temporal.md": NCL,
    "b/branching-time.md": NCL, "l/logic-conditionals.md": NCL,
    "l/logic-connexive.md": NCL, "l/logic-deontic.md": NCL,
    "l/logic-dependence.md": NCL, "l/logic-dialogical.md": NCL,
    "d/dynamic-epistemic.md": NCL, "l/logic-free.md": NCL, "l/logic-fuzzy.md": NCL,
    "l/logic-if.md": NCL, "l/logic-intensional.md": NCL,
    "l/logic-intuitionistic.md": NCL, "t/typelogical-grammar.md": NCL,
    # —— 法哲学与政治哲学
    "e/evidence-legal.md": LAWP, "c/causation-law.md": LAWP,
    "l/law-ideology.md": LAWP, "i/ideology.md": PTHEORY,
    # —— 认识论
    "l/logical-empiricism.md": SPH,
    "e/empiricism-ancient-medieval.md": EPIS + ("知识论",),
    "r/rationalism-empiricism.md": EPIS + ("知识论",),
    "c/certainty.md": EPIS + ("知识论",), "e/epistemology.md": EPIS + ("知识论",),
    "e/epistemology-bayesian.md": EPIS + ("知识论",),
    "e/epistemology-virtue.md": EPIS + ("知识论",),
    "f/formal-epistemology.md": EPIS + ("知识论",),
    "c/common-knowledge.md": EPIS + ("知识论",), "a/abduction.md": EPIS + ("知识论",),
    "c/contextualism-epistemology.md": EPIS + ("知识论",),
    "i/induction-problem.md": EPIS + ("知识论",),
    "k/knowledge-how.md": EPIS + ("知识论",),
    "u/understanding.md": EPIS + ("知识论",),
    "c/closure-epistemic.md": EPIS + ("知识论",),
    "e/epistemic-paradoxes.md": EPIS + ("知识论",),
    "e/epistemic-utility.md": EPIS + ("知识论",),
    "f/fitch-paradox.md": EPIS + ("知识论",),
    "k/knowledge-acquaindescrip.md": EPIS + ("知识论",),
    "k/knowledge-analysis.md": EPIS + ("知识论",),
    "k/knowledge-value.md": EPIS + ("知识论",),
    "s/skepticism-medieval.md": EPIS + ("怀疑论",),
    "t/transmission-justification-warrant.md": EPIS + ("信念与证成",),
    "r/reliabilism.md": EPIS + ("信念与证成",),
    "i/intuition.md": EPIS + ("证据与合理性",),
    "s/self-locating-beliefs.md": EPIS + ("证据与合理性",),
    "e/evidence.md": EPIS + ("证据与合理性",),
    "h/higher-order-evidence.md": EPIS + ("证据与合理性",),
    # —— 形而上学
    "n/naturalism-moral.md": ETH + ("元伦理学",),
    "l/lawphil-naturalism.md": LAWP,
    "i/identity.md": IDENT, "i/identity-indiscernible.md": IDENT,
    "i/identity-time.md": IDENT, "i/identity-relative.md": IDENT,
    "i/identity-transworld.md": IDENT, "i/intrinsic-extrinsic.md": IDENT,
    "i/identity-personal.md": IDENT, "i/identity-ethics.md": IDENT,
    "r/relations.md": IDENT,
    "c/causation-metaphysics.md": CAUS, "c/causation-probabilistic.md": CAUS,
    "d/determinism-causal.md": CAUS, "c/causation-backwards.md": CAUS,
    "c/causation-counterfactual.md": CAUS,
    # —— 宗教哲学
    "r/religion-science.md": REL + ("宗教与科学",),
}

EXTRA.update({
    "w/wittgenstein.md": ANA + ("早期分析哲学",),
    "t/turing.md": INFO,
    "g/green.md": (W, N, "英国唯心论与实在论"),
    "f/feminism-psychoanalysis.md": PHIL + ("女性主义哲学", "女性主义理论"),
    "f/feminism-liberal.md": PHIL + ("女性主义哲学", "女性主义理论"),
})

EXTRA.update({
    # 经济哲学节的博弈论条目归决策与博弈论
    "g/game-theory.md": PHIL + ("决策与博弈论",),
    "e/epistemic-game.md": PHIL + ("决策与博弈论",),
    "g/game-ethics.md": PHIL + ("决策与博弈论",),
    "g/game-evolutionary.md": PHIL + ("决策与博弈论",),
    # 上帝存在的论证：从基督教神学节收拢
    "c/cosmological-argument.md": REL + ("上帝存在的论证",),
    "m/moral-arguments-god.md": REL + ("上帝存在的论证",),
    "d/divine-freedom.md": REL + ("神学与教义",),
    # 正义与健康
    "j/justice-inequality-health.md": POL + ("正义理论",),
    # 认识论：证言与记忆
    "t/testimony-episprob.md": EPIS + ("知识论",),
    "m/memory-episprob.md": EPIS + ("知识论",),
    # 经典逻辑
    "l/logic-classical.md": LANG + ("经典逻辑与传统逻辑",),
    # 科学进步与革命
    "s/scientific-progress.md": SPR,
    "s/scientific-revolutions.md": SPR,
    # 动物意识归认知科学哲学
    "c/consciousness-animal.md": COG,
    # 环境哲学
    "e/ethics-environmental.md": PHIL + ("环境哲学",),
    "j/justice-climate.md": PHIL + ("环境哲学",),
    "c/climate-science.md": PHIL + ("环境哲学",),
    "e/environmental-aesthetics.md": PHIL + ("环境哲学",),
})

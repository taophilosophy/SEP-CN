/* zcode-workflow
description: J 组 38 词条 40 路滚动翻译波（clear→s3_checked），长线后台工作流，确定性分诊+门禁
*/

const SLUGS = [
  "jaina-philosophy", "james", "james-mill", "james-viterbo", "james-ward",
  "japanese-aesthetics", "japanese-confucian", "japanese-philosophy",
  "japanese-pure-land", "japanese-zen", "jaspers", "jayaraasi", "jefferson",
  "joane-petrizi", "johann-fichte", "johann-herbart", "johann-sturm",
  "john-italos", "john-norris", "john-salisbury", "jury-theorems",
  "justep-coherence", "justep-foundational", "justep-intext", "justice",
  "justice-bad-luck", "justice-climate", "justice-distributive",
  "justice-global", "justice-healthcareaccess", "justice-inequality-health",
  "justice-intergenerational", "justice-moral-psych", "justice-retributive",
  "justice-transitional", "justice-virtue", "justification-public",
  "justus-lipsius",
];

const TASK_INSTRUCTIONS = (slug: string) =>
  `你是 SEP-CN 中文翻译项目的重译员，负责词条 ${slug} 的重译（retranslate），目标状态 s3_checked。

【任务】把英文源译成简体中文，零信任：以 yuanwen/j/${slug}.md（英文逐字符镜像，ADR-0009）为唯一翻译底稿，en/${slug}/index.html（若有）为可疑处回源核对。严禁参考任何既有中文译文或缓存。

【严格步骤】
1. 读方向：读 yuanwen/j/${slug}.md、SUMMARY.md 中该词条行、baseline/entries.json 中该 slug 条目（取 pubinfo 日期/存档版/SHA-256 作版本钉）。
2. 清空：python tools/task_ops.py clear ${slug}（基线哈希门禁自动检查；仅保留 H1）。若状态已非 pending，跳过（幂等）。
3. 初译（draft）：按 specs/005-translation-campaign/fan-yi-mu-ban.md §2 元素映射 + §4 骨架，以英文源为唯一底稿从头翻译。每段产出反思式两步账本：tasks/j/${slug}.ledger.yaml（version:1, slug, segments:[{id, source, step1, step2}]），step1=忠实初译，step2=语言优化成稿（ADR-0021 强制）。
4. 一校（s1 准确性）：对照 yuanwen 逐节核销漏译/错译/事实错误（人名、年代、编号）。MTPE 顺序（ADR-0020）：先查幻觉/漏译/增译→术语漂移→语言欧化。
5. 二校（s2 语言）：消除欧化句/倒装/死译（rules/02 反欧化条款）。跑 python tools/check_prose.py ${slug} 看告警逐条改写。
6. 三校（s3 体例）：python tools/check_style.py j/${slug}.md、python tools/check_academic.py --docs j/${slug}.md --strict、python tools/check_math.py ${slug}。s3 advance 时学术门禁自动挂钩（task_ops 内部跑 check_academic --strict，未过拒绝）。
7. 推进：python tools/task_ops.py advance ${slug} --step draft --actor "j-子代理" --evidence "初译完成：零信任译自 yuanwen/j/${slug}.md，账本双版（step1/step2）齐全"；然后 --step s1（对照记录）、--step s2（check_prose 告警清零或逐条豁免留痕）、--step s3（学术+体例双绿）。若某步失败，用 task_ops show ${slug} 确认当前状态，并如实说明。

【体例硬性要点（rules/02，违规返工）】中文弯引号“ ”‘ ’；禁英文直引号/直角引号（U+300C-300F）；中英文/中文数字间半角空格；中文强调用**加粗**不用斜体（italic-cjk），拉丁/希腊字母术语保留斜体；**星号内侧禁空格；禁 HTML；表格居中 :---: 紧凑；数学 $…$ 定界符逐字符保留；引用组 (Author year, p. X) 原样；参考文献非中文条目照录不译、中国文献条目（古今）译为中文（ADR-0011）；文首斜体说明行；节标题 ## 参考文献；脚注 [^note-N] 键名与 yuanwen 逐字符一致；尾部节序固定；版本事实行日期与 baseline pubinfo 一致；学术工具三行链接原样。

【术语纪律（rules/03）】新术语先登记 yi-zhe-shuo-ming.md 后使用（五列：原文/译法/首现/依据/裁定日期），依据=知网系权威源→权威译本→学界惯例，禁维基译名，查无可查保留英文登记，不臆造。人名以 ren-ming-biao.md 为准。同一词条内锁定主形（ADR-0020）。

【禁止】不 git 提交、不 push、不写其他词条、不动 SUMMARY/登记册（只加本词条新术语行）、不改 baseline/en/yuanwen、不造备份、不批量替换。

完成后用 3-5 句话报告：最终 task_ops show ${slug} 的状态、账本段数、check_style/check_academic 结果，以及任何未能完成的原因。禁止虚报。`;

// 确定性分诊：读任务实际状态，不信任子代理自述
async function isS3(slug: string): Promise<boolean> {
  const st = await world.run("python", ["tools/task_ops.py", "show", slug], {
    output: { tail: 4096 }, timeoutMs: 120000,
  });
  return st.exitCode === 0 && st.stdout.includes('"state": "s3_checked"');
}

artifact.board("board", {
  title: "J 组 38 词条翻译波进度",
  key: "slug",
  status: "status",
  columns: ["pending", "done", "retry", "failed"],
  cardTitle: "slug",
  detail: [{ field: "note", label: "说明" }],
});

// 第一轮：全部 fresh
phase("派发 J 组翻译波第一轮");
const round1 = await Promise.allSettled(
  SLUGS.map((slug) => agent(`译·${slug}`).ask<string>(TASK_INSTRUCTIONS(slug))),
);

const done: string[] = [];
const retry: string[] = [];
const failed: { slug: string; note: string }[] = [];
for (let i = 0; i < SLUGS.length; i++) {
  const slug = SLUGS[i];
  const r = round1[i];
  if (r.status === "rejected") {
    retry.push(slug);
    failed.push({ slug, note: `第一轮子代理异常：${String(r.reason).slice(0, 160)}` });
    report({ slug, status: "failed", note: "第一轮子代理异常" }, "board");
    continue;
  }
  const ok = await isS3(slug);
  if (ok) {
    done.push(slug);
    report({ slug, status: "done", note: "第一轮 s3_checked" }, "board");
  } else {
    retry.push(slug);
    failed.push({ slug, note: `第一轮未达 s3（子代理自述：${r.value.slice(0, 100)}）` });
    report({ slug, status: "retry", note: "第一轮未达 s3" }, "board");
  }
}

// 第二轮：fresh 重译未达标的（C 批实测 fresh 优于 resume）
if (retry.length > 0) {
  phase("派发 J 组翻译波第二轮（重试，有界）");
  const round2 = await Promise.allSettled(
    retry.map((slug) => agent(`译重·${slug}`).ask<string>(TASK_INSTRUCTIONS(slug))),
  );
  for (let i = 0; i < retry.length; i++) {
    const slug = retry[i];
    const r = round2[i];
    if (r.status === "rejected") {
      failed.push({ slug, note: `第二轮子代理异常：${String(r.reason).slice(0, 160)}` });
      report({ slug, status: "failed", note: "第二轮子代理异常" }, "board");
      continue;
    }
    const ok = await isS3(slug);
    if (ok) {
      done.push(slug);
      report({ slug, status: "done", note: "第二轮 s3_checked" }, "board");
    } else {
      report({ slug, status: "failed", note: "二轮仍未达 s3，待人工" }, "board");
    }
  }
}

phase("验证门禁并提交");
const finalDone = [...new Set(done)];
const findings = [];
for (const s of finalDone) {
  const acad = await world.run("python", [
    "tools/check_academic.py", "--docs", `j/${s}.md`, "--strict",
  ], { output: { tail: 2048 }, timeoutMs: 120000 });
  const style = await world.run("python", [
    "tools/check_style.py", `j/${s}.md`,
  ], { output: { tail: 2048 }, timeoutMs: 120000 });
  if (acad.exitCode === 0 && style.exitCode === 0) {
    await world.run("git", [
      "add", `j/${s}.md`, `tasks/j/${s}.json`, `tasks/j/${s}.ledger.yaml`,
    ], { timeoutMs: 60000 });
    await world.run("git", [
      "commit", "-m", `j 批 ${s} 初译三校完成（s3_checked）：零信任译自英文源`,
    ], { timeoutMs: 60000, output: "discard" });
    findings.push({
      where: `j/${s}.md`,
      what: `J 组词条 ${s} 达成 s3_checked（初译三校完成）`,
      evidence: "check_academic --strict 0 硬错误 + check_style 0 问题 + task_ops show s3_checked",
      status: "verified" as const,
      severity: "low" as const,
    });
  } else {
    findings.push({
      where: `j/${s}.md`,
      what: `J 组词条 ${s} 达 s3_checked 但收口门禁未过（acad=${acad.exitCode} style=${style.exitCode}）`,
      evidence: `check_academic exit=${acad.exitCode}; check_style exit=${style.exitCode}`,
      status: "unconfirmed" as const,
      severity: "high" as const,
    });
  }
}
for (const f of failed) {
  findings.push({
    where: `j/${f.slug}.md`,
    what: `J 组词条 ${f.slug} 未达 s3_checked`,
    evidence: f.note,
    status: "unconfirmed" as const,
    severity: "medium" as const,
  });
}

const notDone = SLUGS.filter((s) => !finalDone.includes(s));
return {
  conclusion: `J 组翻译波：38 词条中 ${finalDone.length} 达成 s3_checked；${notDone.length} 未达标（${notDone.join(", ")}）。`,
  findings,
  verified: ["每个 s3_checked 词条：world.run task_ops show 确定性分诊 + check_academic --strict + check_style 三重门禁"],
  notCovered: notDone.length > 0
    ? [`以下词条未达 s3_checked，需人工/后续轮处理：${notDone.join(", ")}`]
    : [],
};

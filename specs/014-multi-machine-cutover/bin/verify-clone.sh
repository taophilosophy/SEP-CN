#!/usr/bin/env bash
# 014 迁移验收脚本：在 C:\Users\ykla\Documents\SEP-CN 克隆根目录运行
# 用法: bash specs/014-multi-machine-cutover/bin/verify-clone.sh [--skip-gate]
set -u

fail=0
ok()  { printf '[OK ] %s\n' "$1"; }
bad() { printf '[BAD] %s\n' "$1"; fail=$((fail+1)); }

[ -d .git ] || { echo "请在仓库根目录运行"; exit 2; }
[ -f tools/check_all.py ] || { echo "不是 SEP-CN 仓库根目录"; exit 2; }

# 刚 clone 完 index 未刷新，直接数 git status 会把 racy-git 误报成几十项脏
git update-index --refresh >/dev/null 2>&1 || true

# 1. 与 origin/main 的关系
git fetch --quiet origin 2>/dev/null || bad "git fetch 失败（网络/凭据）"
behind=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo x)
[ "$behind" = 0 ] && ok "HEAD 未落后 origin/main" || bad "落后 origin/main ${behind} 个提交"

# 2. 工作树干净（本地相均被 .gitignore，不应出现）
dirty=$(git status --porcelain | wc -l | tr -d ' ')
[ "$dirty" = 0 ] && ok "工作树干净" || bad "工作树有 ${dirty} 项未提交/未忽略文件"

# 3. 本地相
[ -d en ]      && ok "en/ 存在（顶层 $(ls en | wc -l | tr -d ' ') 项）"            || bad "en/ 缺失"
[ -d yuanwen ] && ok "yuanwen/ 存在（顶层 $(ls yuanwen | wc -l | tr -d ' ') 项）" || bad "yuanwen/ 缺失"
[ -d script ]  && ok "script/ 存在"      || bad "script/ 缺失（个人草稿区）"
[ -d state ]   && ok "state/ 存在"       || bad "state/ 缺失（运行态）"
[ -f .secrets/termonline-session.json ] && ok ".secrets/ 已搬（termonline）" || bad ".secrets/ 缺失"
[ -d node_modules ] && ok "node_modules/ 已装" || bad "node_modules/ 缺失（bun install）"

# 4. 与 D: （M2）文件数比对（可访问时）
if [ -d /d/SEP-CN/en ]; then
  a=$(ls /d/SEP-CN/en | wc -l | tr -d ' '); b=$(ls en | wc -l | tr -d ' ')
  [ "$a" = "$b" ] && ok "en/ 条目数与 M2 一致（${a}）" || bad "en/ 条目数 ${b} != M2 ${a}（M2 可能刚抓取，重跑拷贝）"
else
  printf '[SKIP] D: 不可访问，跳过与 M2 的比对\n'
fi

# 5. 门禁
if [ "${1:-}" = "--skip-gate" ]; then
  printf '[SKIP] 跳过 check_all\n'
else
  log=$(mktemp)
  if python tools/check_all.py --all >"$log" 2>&1; then
    ok "check_all --all 9/9 全绿"
  else
    bad "check_all --all 失败（日志：$log）"
    tail -20 "$log"
  fi
fi

echo
if [ "$fail" = 0 ]; then
  echo "== 验收通过：可以进入 runbook §5（记忆迁移）与 §6（切换封口）"
  exit 0
else
  echo "== 验收未通过：${fail} 项失败，按 runbook 修复后再跑；不得进入切换步骤"
  exit 1
fi

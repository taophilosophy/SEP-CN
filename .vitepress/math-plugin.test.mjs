// math-plugin.mjs protectMath 回归测试（specs/024 复核后修复锁定）
// 跑法：node --test .vitepress/math-plugin.test.mjs
import { test } from 'node:test'
import assert from 'node:assert/strict'
import { protectMath } from './math-plugin.mjs'

const b64d = (s) => Buffer.from(s, 'base64url').toString('utf8')
const sentinels = (src) => (src.match(/@@MJ([A-Za-z0-9_-]+)@@/g) || [])

/** 输出里的公式原文清单（哨兵解码还原） */
function formulas(out) {
  return sentinels(out).map((s) => b64d(s.slice(4, -2)))
}

test('A 支修复：数字开头 + 尾部空格公式受保护（frege-theorem L503 实证形态）', () => {
  const line =
    '- 1 is the number of the concept *author of Principia Mathematica other than Russell*, i.e.,     $1 = \\#[\\lambda z \\, Azp \\amp z\\neqclose r] $'
  const out = protectMath(line)
  const fs = formulas(out)
  assert.equal(fs.length, 1, `应有 1 个哨兵，实际 ${fs.length}: ${out.slice(0, 120)}`)
  assert.equal(fs[0], '$1 = \\#[\\lambda z \\, Azp \\amp z\\neqclose r] $', '公式原文应无损还原')
})

test('A 支不回归：尾部紧随形态仍保护', () => {
  const out = protectMath('$2 = \\#[\\lambda z \\, Azp]$')
  assert.equal(formulas(out).length, 1)
})

test('B 支修复：首字符空白 + 圆括号（anaphora/game-evolutionary 实证形态）', () => {
  const out = protectMath('Boethius’ theses: $ (A \\to B) \\to \\neg (A \\to \\neg B)$ and $ (A \\to \\neg B) \\to \\neg (A \\to B) $')
  const fs = formulas(out)
  assert.equal(fs.length, 2, `应配 2 个公式，实际 ${fs.length}: ${out.slice(0, 160)}`)
  assert.ok(fs.every((f) => f.startsWith('$ (') && f.endsWith('$')), '公式含原文空白')
})

test('B 支不回归：原子译稿形态仍保护', () => {
  const out = protectMath("$ \\alpha S' = {…} $")
  assert.equal(formulas(out).length, 1)
})

test('货币守卫：$150,000 and $200,000 不配对', () => {
  const out = protectMath('It costs $150,000 and $200,000 respectively.')
  assert.equal(sentinels(out).length, 0, `货币不得配成公式: ${formulas(out)}`)
  assert.ok(out.includes('$150,000'), '货币文本原样')
})

test('货币守卫：闭合 $ 后跟数字仍拒绝', () => {
  const out = protectMath('pay $150 and get $3 back')
  assert.equal(sentinels(out).length, 0)
})

test('display 块 $$ 不回归', () => {
  const out = protectMath('$$\n\\begin{align*} x = y \\end{align*}\n$$')
  assert.equal(formulas(out).length, 1)
  assert.ok(formulas(out)[0].startsWith('$$'))
})

test('围栏代码块内 $ 原样保留', () => {
  const src = '```\nprice is $100 and $200\n```'
  const out = protectMath(src)
  assert.equal(sentinels(out).length, 0)
  assert.ok(out.includes('$100'))
})

test('行内代码内 $ 原样保留', () => {
  const out = protectMath('use `$1 = \\#2 $` literally')
  assert.equal(sentinels(out).length, 0)
})

test('非白名单尖括号转义不回归（既有语义：只转义 <，> 为普通文本）', () => {
  const out = protectMath('the <Socrates> case')
  assert.ok(out.includes('&lt;Socrates>'), out)
})

test('白名单尖括号原样放行不回归', () => {
  const out = protectMath('<em>x</em>')
  assert.ok(out.includes('<em>x</em>'), out)
})

test('连续公式行保护后哨兵彼此独立（防连锁错配）', () => {
  const out = protectMath('$ a \\to b $ then $ c \\to d $ then $ e $')
  assert.equal(formulas(out).length, 3)
})

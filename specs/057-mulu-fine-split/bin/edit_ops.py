#!/usr/bin/env python3
"""specs/057 s3l：B 类结构修正的通用编辑原语（改名／移条／升格／去壳／删空节）。

指令 JSON（数组，按序执行；每步重读文件，避免行号漂移）：
  {"op":"rename","path":"甲／乙","to":"新名"}
  {"op":"move_entry","from":"甲／乙","slug":"x","to":"丙／丁"[,"sub":"子节名"]}
       sub 不存在则在目标节点末尾新建该子节；否则追加到该子节条目末尾
  {"op":"promote","path":"甲／乙／丙","after":"同级锚名","level":3}
       把节点整块剪切，改标题层级，插到父节点下锚节点之后
  {"op":"unwrap","path":"甲／乙／丙"}
       删除该标题行，内容上提到父节点标题之后（作为直属）
  {"op":"delete_empty","path":"甲／乙／丙"}
       节点整子树无条目则删除（含尾部空行）
最后统一压缩多余空行（保留首数据段原有双空行）并断言链接行守恒 1883。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
H = re.compile(r"^(#{1,6}) (.+?)\s*$")
E = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")


def parse(lines):
    heads, stack = [], []
    for i, l in enumerate(lines):
        m = H.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= lv:
                stack.pop()
            p = tuple(x[1] for x in stack) + (t,)
            heads.append((i, lv, p))
            stack.append((lv, t))
    return heads


def find(heads, path):
    hits = [(i, lv) for i, lv, p in heads if p == path]
    assert len(hits) == 1, f"{'／'.join(path)} 命中 {len(hits)} 处"
    return hits[0]


def end_of(lines, heads, li, lv):
    for i, l2, _ in heads:
        if i > li and l2 <= lv:
            return i
    return len(lines)


def entry_block(lines, lo, hi, slug):
    """区间内直属母条块（母条＋连续缩进子条），返回 (start, stop) 或 None。"""
    for k in range(lo, hi):
        m = E.match(lines[k])
        if m and len(m.group(1)) == 0 and m.group(3).rsplit("/", 1)[-1][:-3] == slug:
            j = k + 1
            while j < hi and (mm := E.match(lines[j])) and len(mm.group(1)) > 0:
                j += 1
            return k, j
    return None


def first_sub(lines, heads, li, lv, hi):
    for i, l2, _ in heads:
        if li < i < hi and l2 == lv + 1:
            return i
    return None


def insert_block(lines, pos, block):
    pad = []
    if pos > 0 and lines[pos - 1] != "":
        pad.append("")
    lines[pos:pos] = pad + block
    return pos + len(pad) + len(block)


def main():
    ops = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    for op in ops:
        lines = MULUS.read_text(encoding="utf-8").splitlines()
        heads = parse(lines)
        key = op["op"]
        if key == "rename":
            path = tuple(op["path"].split("／"))
            li, lv = find(heads, path)
            lines[li] = "#" * lv + " " + op["to"]
        elif key == "move_entry":
            src = tuple(op["from"].split("／"))
            dst = tuple(op["to"].split("／"))
            sli, slv = find(heads, src)
            send = end_of(lines, heads, sli, slv)
            got = entry_block(lines, sli + 1, send, op["slug"])
            assert got, f"{op['from']} 内无母条 {op['slug']}"
            a, b = got
            block = lines[a:b]
            del lines[a:b]
            heads = parse(lines)  # 行号已变，重解析
            dli, dlv = find(heads, dst)
            dend = end_of(lines, heads, dli, dlv)
            sub = op.get("sub")
            if sub:
                subhits = [(i, l2) for i, l2, p in heads
                           if li_ok(i, dli, dend) and p[-1] == sub and l2 == dlv + 1]
                if subhits:
                    si, sl = subhits[0]
                    send = end_of(lines, heads, si, sl)
                    insert_block(lines, send, [""] + block + [""])
                else:
                    pos = dend
                    lines[pos:pos] = ["", "#" * (dlv + 1) + " " + sub, ""] + block + [""]
            else:
                fs = first_sub(lines, heads, dli, dlv, dend)
                pos = fs if fs is not None else dend
                insert_block(lines, pos, block + [""])
        elif key == "promote":
            path = tuple(op["path"].split("／"))
            li, lv = find(heads, path)
            hi = end_of(lines, heads, li, lv)
            block = lines[li:hi]
            newlv = op["level"]
            block[0] = "#" * newlv + " " + path[-1]
            del lines[li:hi]
            while li < len(lines) and lines[li] == "":
                del lines[li]
            heads = parse(lines)
            parent = path[:-2]                      # 上两级（如 H2）
            pli, plv = find(heads, parent)
            pend = end_of(lines, heads, pli, plv)
            anchor = op.get("after") or path[-2]
            pos = pend
            for i, l2, p in heads:
                if li_ok(i, pli, pend) and l2 == plv + 1 and p[-1] == anchor:
                    pos = end_of(lines, heads, i, l2)
                    break
            else:
                raise AssertionError(f"锚 {anchor} 不在 {'／'.join(parent)} 下")
            insert_block(lines, pos, [""] + block + [""])
        elif key == "unwrap":
            path = tuple(op["path"].split("／"))
            li, lv = find(heads, path)
            hi = end_of(lines, heads, li, lv)
            content = [l for l in lines[li + 1:hi] if l != ""]
            del lines[li:hi]
            pli, plv = find(parse(lines), path[:-1])
            heads = parse(lines)
            fs = first_sub(lines, heads, pli, plv, end_of(lines, heads, pli, plv))
            pos = fs if fs is not None else end_of(lines, heads, pli, plv)
            lines[pos:pos] = [""] + content + [""]
        elif key == "delete_empty":
            path = tuple(op["path"].split("／"))
            li, lv = find(heads, path)
            hi = end_of(lines, heads, li, lv)
            assert not any(E.match(l) for l in lines[li + 1:hi]), f"{op['path']} 非空"
            del lines[li:hi]
            while li < len(lines) and lines[li] == "":
                del lines[li]
        else:
            raise SystemExit(f"未知 op {key}")
        MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        print("ok", key, op.get("path") or (op.get("from"), op.get("slug"), op.get("to")))

    # 统一压缩多余空行（保留首个双空行段，即 0 基 18 行）
    lines = MULUS.read_text(encoding="utf-8").splitlines()
    out = []
    for i, l in enumerate(lines):
        if l == "" and out and out[-1] == "" and i != 18:
            continue
        out.append(l)
    n = sum(1 for l in out if E.match(l))
    assert n == 1883, f"守恒破坏：{n}"
    MULUS.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print("守恒", n)


def li_ok(i, lo, hi):
    return lo < i < hi


if __name__ == "__main__":
    sys.exit(main())

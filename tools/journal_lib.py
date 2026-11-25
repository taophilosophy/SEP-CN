# -*- coding: utf-8 -*-
"""journal 事件写入原语（ADR-0068 W3 双写）：task_ops 与 journal_migrate 共用。

职责单一：把 task_ops 的 step 名映射为六类事件，并只追加写入 journal/<letter>/<slug>.ndjson。
写路径零信任：复用 common.write_text_verified（读回比对，SMB 假成功防护）。
不包含任何状态机逻辑（ORDER 推导在 task_ops）。
"""
import io
import json
import os
import sys

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

from tools.common import read_text, repo_path, write_text_verified  # noqa: E402
from tools import naming_lib  # noqa: E402

# step 拼写（identifier／name／历史别名／CLI 短名）→ 节点 identifier（ADR-0080）。
# 新事件一律写 identifier；旧事件里的历史名经同一张表反查。
NODE_MAP = dict(naming_lib.load()["_by_alias"])

# 节点 identifier → 状态名（identifier＋_checked；旧状态名进 naming.json 的 state_aliases）
NODE_TO_STATE = {n["identifier"]: n["state"]
                 for n in naming_lib.load().get("nodes", []) if n.get("state")}

# 回退 checkpoint：从这些节点重走（对应 ADR-0043/0063 的受控回退语义）
REVERT_CHECKPOINTS = tuple(naming_lib.load().get("revert_checkpoints") or ())

JOURNAL_DIR = None  # 可注入（测试用）；默认 <repo>/journal


def _journal_path(slug):
    letter = slug[0] if slug and slug[0].isalnum() else "0"
    base = JOURNAL_DIR or repo_path("journal")
    return os.path.join(base, letter, slug + ".ndjson")


def read_events(slug):
    """读一个条目的全部事件（无文件返回空列表）。"""
    path = _journal_path(slug)
    if not os.path.exists(path):
        return []
    out = []
    for line in read_text(path).splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def append_event(slug, event):
    """只追加一个事件（P5）；seq 自动递增；写后读回校验（A14/P27）。"""
    path = _journal_path(slug)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    existing = read_text(path) if os.path.exists(path) else ""
    max_seq = 0
    for line in existing.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            max_seq = max(max_seq, int(json.loads(line).get("seq", 0)))
        except (json.JSONDecodeError, ValueError):
            pass
    if "seq" not in event:
        event["seq"] = max_seq + 1
    line = json.dumps(event, ensure_ascii=False) + "\n"
    write_text_verified(path, existing + line)
    return event


def step_to_event(step_name, evidence="", at="", actor="migrate", attempt="main"):
    """task_ops 的 step 名 → journal 事件；非节点动作返回 None（跳过）。

    与 journal_migrate._map_step 同源：pass 对应节点；revert/reopen/rework 对应 rework；
    done/clear/block/reset 等非节点动作不落 journal（done 是派生量）。
    """
    if step_name in NODE_MAP:
        return {"type": "pass", "node": NODE_MAP[step_name], "gate": [],
                "at": at, "actor": actor, "attempt": attempt}
    if step_name == "revert-state":
        import re
        to = None
        m = re.search(r"回退到\s*([A-Za-z0-9._\-]+)", evidence or "")
        if m:
            # 证据文本可能是旧状态名或新状态名：统一经 naming.json 归一到 identifier
            to = naming_lib.node_of_state(m.group(1))
        return {"type": "rework", "from_node": to,
                "reason": (evidence or "")[:200],
                "at": at, "actor": actor, "attempt": attempt}
    if step_name == "reopen" or (step_name and step_name.startswith("rework")):
        return {"type": "rework", "from_node": None,
                "reason": (evidence or "")[:200],
                "at": at, "actor": actor, "attempt": attempt}
    return None

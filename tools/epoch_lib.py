# -*- coding: utf-8 -*-
"""进度纪元（ADR-0081）：全库置空后，进度视图只统计本纪元及之后的事件。

journal 是事实，不删不改（P5／ISO 15489-1）；纪元是**声明**，不是改写——
`rules/epoch.json` 记录 current_epoch，视图据此过滤。历史 pass 仍在 journal 里，
可随时用更早的纪元或空纪元复核。
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPOCH_PATH = os.path.join(ROOT, "rules", "epoch.json")


def start(path=None):
    """返回 current_epoch（ISO 8601 Z 串）；无纪元文件返回 None（不过滤）。"""
    p = path or EPOCH_PATH
    if not os.path.exists(p):
        return None
    with open(p, "rb") as f:
        return json.loads(f.read().decode("utf-8")).get("current_epoch")


def in_epoch(event, epoch=None):
    """事件是否属于当前纪元（无纪元或事件缺 at 时按属于处理，避免误删旧账）。"""
    ep = epoch if epoch is not None else start()
    if not ep:
        return True
    at = str(event.get("at") or "")
    return at >= ep if at else True

# -*- coding: utf-8 -*-
"""跨机收编件记账与回炉（specs/052 §2，ADR-0075）。

对象：`state=cleared` 但正文已在库的件（2026-11-13 跨机 WIP 收编的直接后果）。
clear 的语义是"正文置空"，所以这 18 件的账实不符不是"状态旧"，而是**正文在
clear 之后入库且无任何过程记录**——它们既逃过全部体例门禁（cleared 不在
GATE_STATES），又不被任何批次选中。

处置（用户 2026-11-19 批准第 2 条）：
  1. 补记 import 事件：synthetic（事后补记）、basis=state、state_at_import=cleared，
     note 记正文首次入库提交 / 日期 / sha256 / 汉字数——**不推断中间节点**。
  2. 回炉：advance s0（真跑 en_integrity＋en_source_audit）→ advance draft，
     进入 s1 队列。截断件停在 s0_source_checked 并置 block（不谎称"初译完成"）。
  3. 哈希不符即拒（零信任：调查后文件又变过，说明凭证过期，须重新调查）。

用法:
  python specs/052-mandatory-backfill/bin/adopt_import.py --data <provenance.json>
  python specs/052-mandatory-backfill/bin/adopt_import.py --data <...> --apply
缺省只读；--apply 才写 journal 与任务状态。退出码 0 全处理；1 有拒办件。
"""
import argparse
import json
import os
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

from tools.common import sha256_file, utcnow_iso, write_text_verified  # noqa: E402
from tools.journal_lib import append_event, read_events  # noqa: E402
from tools.task_ops import (PreconditionError, UsageError, advance, block,  # noqa: E402
                            load_task)

DATE = datetime.now().strftime("%Y-%m-%d")
ACTOR = "adopt-" + DATE


def _import_recorded(events, slug):
    return any(e.get("type") == "import" and str(e.get("note") or "").startswith("adopt:" + DATE)
               for e in events)


def process(rec, apply=False):
    slug = rec["slug"]
    out = {"slug": slug, "status": "", "detail": ""}
    task = load_task(slug)
    if not task:
        out.update(status="refused", detail="任务不存在")
        return out
    if task.get("state") != "cleared":
        out.update(status="skip", detail="状态已非 cleared：%s" % task.get("state"))
        return out
    zh = task.get("zh_doc") or rec.get("zh_doc")
    full = zh if os.path.isabs(zh) else os.path.join(ROOT, zh)
    if not os.path.exists(full):
        out.update(status="refused", detail="译文缺失：%s" % zh)
        return out
    actual = sha256_file(full)
    if actual != rec["sha256"]:
        out.update(status="refused",
                   detail="哈希不符（调查时 %s… 现 %s…）：凭证过期，重新调查"
                          % (rec["sha256"][:12], actual[:12]))
        return out
    if not apply:
        out.update(status="dry-run", detail="将补记 import 并回炉 s0→draft")
        return out
    events = read_events(slug)
    if not _import_recorded(events, slug):
        append_event(slug, {
            "type": "import", "synthetic": True, "basis": "state",
            "state_at_import": "cleared", "attempt": "main", "at": utcnow_iso(),
            "actor": ACTOR,
            "note": "adopt:%s:正文首次入库 %s（%s %s），sha256 %s，%d 汉字；"
                    "clear 早于正文，无过程记录（specs/052，ADR-0075）"
                    % (DATE, rec["first_commit"], rec["first_date"],
                       rec.get("first_subject") or "", rec["sha256"][:16], rec["han"]),
        })
    try:
        advance(slug, "s0", ACTOR,
                "跨机收编回炉（ADR-0075）：正文首次入库 %s（%s，sha256 %s…，%d 汉字）；"
                "s0 门禁本次实跑" % (rec["first_commit"], rec["first_date"],
                                     rec["sha256"][:12], rec["han"]))
        if rec.get("blocked"):
            block(slug, rec["block_reason"] or "正文不完整，待补译")
            out.update(status="blocked", detail="停 s0_source_checked 并置阻塞：%s"
                                              % (rec["block_reason"] or ""))
            return out
        advance(slug, "draft", ACTOR,
                "回炉起点：正文在库 %d 汉字（来源 %s），自 s1 起重走；状态不再声称已清空"
                % (rec["han"], rec["first_commit"]))
        out.update(status="adopted", detail="s0_source_checked → drafted")
    except (PreconditionError, UsageError) as e:
        out.update(status="refused", detail=str(e)[:400])
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--slugs", nargs="*", default=None)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)
    data = json.load(open(args.data, encoding="utf-8"))
    recs = data["entries"]
    if args.slugs:
        recs = [r for r in recs if r["slug"] in set(args.slugs)]
    rows = [process(r, args.apply) for r in recs]
    for r in rows:
        print("%-20s %-8s %s" % (r["slug"], r["status"], r["detail"]))
    out = {"schema": "sep-adopt-result/v1", "date": DATE, "apply": args.apply, "rows": rows}
    name = "adopt-%s%s.json" % (DATE.replace("-", ""), "" if not args.slugs else "-partial")
    path = os.path.join(ROOT, "specs", "052-mandatory-backfill", "results", name)
    write_text_verified(path, json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print("凭证：%s" % os.path.relpath(path, ROOT).replace("\\", "/"))
    return 1 if any(r["status"] == "refused" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""管线公共设施：路径、UTF-8 无 BOM 读写、SHA-256、写后读回自校验。

零信任约束（宪法 I/II）：本仓库位于 SMB 网络映射盘，实测存在"报告写入成功
但文件未落盘"的假成功（见 specs/001-sep-sync-pipeline/plan.md 环境补充约束）。
所有 JSON 落盘必须经 write_json_verified()：写临时文件→读回比对→原子替换→
再读回哈希复核，任何一步不符即抛 OSError。
"""
import hashlib
import io
import json
import os
import sys
import tempfile
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Windows 原生 stdout 在管道下默认 gbk：仅在尚未是 UTF-8 时包装一次
# （重复包装会让旧 TextIOWrapper 被 GC 时关闭底层 buffer——演示轮 2 教训）
def _force_utf8(stream):
    if stream is None:
        return stream
    enc = (getattr(stream, "encoding", "") or "").lower().replace("-", "")
    if enc == "utf8":
        return stream
    try:
        return io.TextIOWrapper(stream.buffer, encoding="utf-8", errors="replace")
    except Exception:
        return stream


sys.stdout = _force_utf8(sys.stdout)
sys.stderr = _force_utf8(sys.stderr)


def repo_path(*parts):
    return os.path.join(ROOT, *parts)


def utcnow_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path):
    """UTF-8 无 BOM 读入；容忍带 BOM 的历史文件但返回已剥离内容。"""
    with open(path, "rb") as f:
        data = f.read()
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    return data.decode("utf-8")


def write_text(path, text):
    """UTF-8 无 BOM、LF 行尾写入。"""
    data = text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)


def write_text_verified(path, text):
    """写文本并读回比对（零信任：SMB 写入可能静默不一致），重试 3 次。"""
    data = text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    last = None
    for attempt in range(3):
        try:
            with open(path, "wb") as f:
                f.write(data)
                f.flush()
                os.fsync(f.fileno())
            with open(path, "rb") as f:
                if f.read() == data:
                    return sha256_bytes(data)
            last = OSError("readback mismatch on %s (attempt %d)" % (path, attempt + 1))
        except OSError as e:
            last = e
        import time
        time.sleep(0.5)
    raise OSError("write_text_verified failed after 3 attempts: %s: %s" % (path, last))


def write_json_verified(path, obj):
    """写入 JSON 并自校验（宪法 I：不信任写入回执）。

    步骤：序列化→写临时文件→读回逐字节比对→os.replace 原子替换→
    最终读回再比对一次。任一环节不符抛 OSError，绝不留半截文件。
    """
    data = json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8")
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=directory, suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        with open(tmp, "rb") as f:
            if f.read() != data:
                raise OSError("write_json_verified: temp file content mismatch: %s" % tmp)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except OSError:
                pass
    with open(path, "rb") as f:
        if f.read() != data:
            raise OSError("write_json_verified: final file content mismatch: %s" % path)
    return sha256_bytes(data)


def load_json(path):
    with open(path, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


def ensure_dirs():
    for d in ("en", "en/_catalog", "baseline", "baseline/changes", "tasks", "script"):
        os.makedirs(repo_path(d), exist_ok=True)


def http_log_path():
    return repo_path("script", "http-log.jsonl")


def find_zh_doc(slug, title_en=None):
    """SUMMARY.md → 中文文档路径（三级匹配，演示轮 2 教训：

    1) 路径以 slug.md 结尾；
    2) slug 首字母目录下、文件名含 slug（子串或分词）——排除 '— see' 别名词条；
    3) 链接文字含英文标题全词（title_en 来自 citation_title）。
    目录型词条（如 s/ji-he-lun-set-theory-joan-bagaria/）按 SUMMARY 实际链接形态匹配。
    """
    import re
    summary = repo_path("SUMMARY.md")
    try:
        text = open(summary, encoding="utf-8-sig").read()
    except FileNotFoundError:
        return None

    def ok(path):
        return "-see-" not in path.lower()

    m = re.search(r"\]\(([^)]*%s\.md)\)" % re.escape(slug), text)
    if m and ok(m.group(1)):
        return m.group(1)
    letter = slug[0]
    cands = []
    # 逐行解析（演示轮 2 复核：链接文字含 \[Abailard\] 转义括号时，
    # finditer 的 \[[^\]]*\] 会在文字中途截断导致整行漏配）
    for line in text.split("\n"):
        pm = re.search(r"\]\(([^)]+)\)", line)
        if not pm:
            continue
        link_text, path = line[:pm.start()], pm.group(1)
        if "-see-" in path.lower() or "-see-" in link_text.lower():
            continue
        # 集群词条链接形如 s/ji-he-lun-set-theory-joan-bagaria/README.md：
        # slug 可能在路径中段，须查整条路径而非仅文件名
        if path.startswith(letter + "/") and (
                slug in path.lower() or slug in path.replace("/", "-").split("-")):
            cands.append(path)
    if cands:
        cands.sort(key=len)
        return cands[0]
    if title_en:
        words = [w.lower() for w in re.findall(r"[A-Za-z]+", title_en) if len(w) > 1]
        if words:
            longest = max(words, key=len)
            hits = []
            for line in text.split("\n"):
                pm = re.search(r"\]\(([^)]+)\)", line)
                if not pm:
                    continue
                link_text, path = line[:pm.start()], pm.group(1)
                if "-see-" in path.lower() or "-see-" in link_text.lower():
                    continue
                hay = (link_text + " " + path.replace("/", " ")).lower()
                if all(w in hay for w in words):
                    hits.append((longest in path.lower(), -len(path), path))
            if hits:
                hits.sort(reverse=True)
                return hits[0][2]
    return None

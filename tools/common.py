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

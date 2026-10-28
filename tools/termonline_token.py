# -*- coding: utf-8 -*-
"""术语在线（termonline）localStorage token 解密工具（specs/008 P0 破译辅助）。

站点前端把 token 存成 AES-CBC-PKCS7 密文（见 index-9a01f905.js 的 cacheCipher），
直接读 localStorage 拿到的是密文，发请求会 401「token非法无效」。本工具把
localStorage 密文还原成明文 JWT，供 cnki_query.py --provider termonline-all
的 --token / TERMONLINE_TOKEN 使用。

用法（Windows Git Bash，粘贴时注意换行）:
  python tools/termonline_token.py "99kv1swmfeFwM/..."
  # 或读文件：
  python tools/termonline_token.py --file token_cipher.txt
  # 明文 JWT 打印到 stdout（无换行尾随）

不落盘明文；密文可由用户从浏览器 console 复制，或本脚本 --from-localstorage
（仅在已打开 termonline 页面时经浏览器环境，本机直跑不支持）。
"""
import base64
import binascii
import io
import json
import sys

KEY = '_11111000001111@'   # cacheCipher.key（16 字节，UTF-8）
IV = '@11111000001001_'    # cacheCipher.iv（16 字节，UTF-8，非 base64）

# ---------------- 纯 Python AES-128-CBC 解密（PKCS7） ----------------
# 自包含 S 盒/逆 S 盒，按 FIPS-197 实现。仅解密，够用。

_SBOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16,
]
_RSBOX = [0] * 256
for _i, _v in enumerate(_SBOX):
    _RSBOX[_v] = _i

_RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8]


def _xtime(a):
    a <<= 1
    if a & 0x100:
        a ^= 0x11b
    return a & 0xff


def _mul(a, b):
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        a = _xtime(a)
        b >>= 1
    return result


def _expand_key(key):
    """AES-128 key expansion：返回 176 字节轮密钥。"""
    nk, nr = 4, 10
    w = [list(key[4 * i:4 * i + 4]) for i in range(nk)]
    for i in range(nk, 4 * (nr + 1)):
        temp = w[i - 1][:]
        if i % nk == 0:
            temp = temp[1:] + temp[:1]
            temp = [_SBOX[b] for b in temp]
            temp[0] ^= _RCON[i // nk - 1]
        elif nk > 6 and i % nk == 4:
            temp = [_SBOX[b] for b in temp]
        w.append([w[i - nk][j] ^ temp[j] for j in range(4)])
    return [b for word in w for b in word]


def _add_round_key(state, rk, r):
    for i in range(16):
        state[i] ^= rk[r * 16 + i]


def _inv_shift_rows(state):
    """行 r 循环右移 r 位（列式存储：index = col*4 + row）。"""
    s = state[:]
    for r in range(4):
        for c in range(4):
            state[c * 4 + r] = s[((c - r) % 4) * 4 + r]


def _inv_sub_bytes(state):
    for i in range(16):
        state[i] = _RSBOX[state[i]]


def _inv_mix_columns(state):
    for c in range(4):
        i = c * 4
        a0, a1, a2, a3 = state[i], state[i + 1], state[i + 2], state[i + 3]
        state[i] = _mul(a0, 14) ^ _mul(a1, 11) ^ _mul(a2, 13) ^ _mul(a3, 9)
        state[i + 1] = _mul(a0, 9) ^ _mul(a1, 14) ^ _mul(a2, 11) ^ _mul(a3, 13)
        state[i + 2] = _mul(a0, 13) ^ _mul(a1, 9) ^ _mul(a2, 14) ^ _mul(a3, 11)
        state[i + 3] = _mul(a0, 11) ^ _mul(a1, 13) ^ _mul(a2, 9) ^ _mul(a3, 14)


def _aes_decrypt_block(block, rk):
    """解密单个 16 字节块（CBC 模式下逐块调用）。"""
    state = list(block)
    _add_round_key(state, rk, 10)
    for rnd in range(9, 0, -1):
        _inv_shift_rows(state)
        _inv_sub_bytes(state)
        _add_round_key(state, rk, rnd)
        _inv_mix_columns(state)
    _inv_shift_rows(state)
    _inv_sub_bytes(state)
    _add_round_key(state, rk, 0)
    return bytes(state)


def _pkcs7_unpad(data):
    if not data:
        raise ValueError('空密文')
    pad = data[-1]
    if pad < 1 or pad > 16 or data[-pad:] != bytes([pad]) * pad:
        raise ValueError('PKCS7 填充非法')
    return data[:-pad]


def aes_cbc_decrypt(cipher_b64, key=KEY, iv=IV):
    """AES-128-CBC 解密（PKCS7 unpad），cipher_b64 为 CryptoJS 输出的 base64。"""
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')
    if len(key_bytes) != 16 or len(iv_bytes) != 16:
        raise ValueError('AES-128 要求 key/iv 各 16 字节')
    try:
        cipher = base64.b64decode(cipher_b64)
    except (binascii.Error, ValueError):
        raise ValueError('密文非合法 base64（请从 localStorage 复制完整值）')
    if len(cipher) % 16 != 0:
        raise ValueError('密文长度非 16 倍数，可能截断')
    rk = _expand_key(key_bytes)
    prev = iv_bytes
    out = bytearray()
    for i in range(0, len(cipher), 16):
        block = cipher[i:i + 16]
        dec = _aes_decrypt_block(block, rk)
        out.extend(bytes(a ^ b for a, b in zip(dec, prev)))
        prev = block
    return _pkcs7_unpad(bytes(out))


def _print_token():
    """输出解密 JSON 的 value（明文 JWT），不带尾随换行，供 shell 捕获。"""
    raw = sys.argv[1]
    if raw.startswith('--file='):
        with open(raw[len('--file='):], encoding='utf-8') as f:
            raw = f.read().strip()
    plain = aes_cbc_decrypt(raw)
    try:
        payload = json.loads(plain)
        token = payload.get('value')
    except (json.JSONDecodeError, AttributeError):
        token = plain
    if not token:
        raise SystemExit('解密结果无 value 字段：%s' % plain[:200])
    sys.stdout.write(token)


if __name__ == '__main__':
    _print_token()

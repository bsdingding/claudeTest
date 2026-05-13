"""
问题：给定一个由 '0' 和 '1' 构成的字符串，求最长的 0 和 1 数量相同的子串的长度。

思路：前缀和 + 哈希表
  - 将 '0' 视为 -1，'1' 视为 +1
  - 对原数组求前缀和 prefix[i]，表示 s[0..i-1] 中 1 的个数减去 0 的个数
  - 若 prefix[i] == prefix[j]（i < j），则 s[i..j-1] 中 0 和 1 数量相等
  - 问题转化为：求前缀和数组中两个相同值之间的最大距离

时间复杂度：O(n)
空间复杂度：O(n)
"""


def find_max_length(s: str) -> int:
    first_seen = {0: -1}
    prefix = 0
    max_len = 0

    for i, ch in enumerate(s):
        prefix += 1 if ch == '1' else -1

        if prefix in first_seen:
            max_len = max(max_len, i - first_seen[prefix])
        else:
            first_seen[prefix] = i

    return max_len


# ── 测试 ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    cases = [
        ("0000111100",  8),
        ("00011100",    6),
        ("000001",      2),
        ("0010011",     6),
        ("0111000111",  8),
        ("01010101010", 10),
        ("110100110001", 12),
        ("0" * 50 + "1" * 50,  100),
        ("0" * 100 + "1" * 99, 198),
    ]

    for s, expected in cases:
        result = find_max_length(s)
        status = "OK" if result == expected else "FAIL"
        print(f"[{status}] s={s!r:12s}  got={result}  expected={expected}")

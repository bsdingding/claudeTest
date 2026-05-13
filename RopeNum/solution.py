"""
问题：N 条绳子，每次随机选 2 个绳头连在一起，直到所有绳头配对完毕，
      求最终绳子（包括环）数量的期望。

推导：设 E(n) 为 n 条绳子时的期望。共 2n 个绳头，取定任意一头，
      随机与剩余 2n-1 个绳头之一配对：
        - 概率 1/(2n-1)  : 与同一条绳的另一头相连 → 成环，剩 n-1 条
        - 概率 (2n-2)/(2n-1): 与另一条绳的绳头相连 → 两绳合一，剩 n-1 条

      E(n) = 1/(2n-1) * (1 + E(n-1)) + (2n-2)/(2n-1) * E(n-1)
           = 1/(2n-1) + E(n-1)

      E(1) = 1（1条绳，2个头连在一起成一个环）

结论：E(N) = 1 + 1/3 + 1/5 + ... + 1/(2N-1)
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def frac_add(p1, q1, p2, q2):
    p = p1 * q2 + p2 * q1
    q = q1 * q2
    g = gcd(abs(p), abs(q))
    return p // g, q // g


def expected_ropes_exact(n: int):
    dp_p, dp_q = 0, 1  # dp[0] = 0/1
    dp_p, dp_q = 1, 1  # dp[1] = 1
    for i in range(2, n + 1):
        dp_p, dp_q = frac_add(dp_p, dp_q, 1, 2 * i - 1)
    return dp_p, dp_q


if __name__ == "__main__":
    print(f"{'N':>4}  {'期望'}")
    print("-" * 20)
    for n in [1, 2, 3, 5, 10, 20, 50, 100]:
        p, q = expected_ropes_exact(n)
        print(f"{n:>4}  {p}/{q}" if q != 1 else f"{n:>4}  {p}")

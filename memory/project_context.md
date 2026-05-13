---
name: project-context
description: 仓库结构、已完成题目、Git 状态
metadata:
  type: project
---

**仓库：** `/Users/bytedance/repos/leetcode`，remote `git@github.com:bsdingding/claudeTest.git`
**Why:** 用于存放算法题解，用 Git 管理，练习标准开发流程。
**How to apply:** 新题建独立目录（如 `RotatedSearch/`），在 feature branch 开发，PR 进 master。

## 已完成题目

| 目录 | 题目 | 算法 |
|---|---|---|
| `str01/` | 01 字符串最长 0/1 相等子串 | 前缀和 + 哈希表，O(n) |
| `RopeNum/` | N 条绳子随机连绳头，求最终绳数期望 | DP：`dp[i] = dp[i-1] + 1/(2i-1)`，手写分数 |
| `RotatedSearch/` | 旋转有序数组查找 target | 二分查找，O(log n) |

## Git 分支结构

- `master`：默认分支（已设为 GitHub default branch）
- `ianding`：第一次误建的分支，内容同 master（遗留，可忽略）
- `ianding_dev`：开发分支，`RotatedSearch` 从这里 PR 合入 master（已 merged）

## 手写工具函数（RopeNum）

```python
def gcd(a, b):
    while b: a, b = b, a % b
    return a

def frac_add(p1, q1, p2, q2):
    p, q = p1*q2 + p2*q1, q1*q2
    g = gcd(abs(p), abs(q))
    return p//g, q//g
```

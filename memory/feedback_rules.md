---
name: feedback-rules
description: 用户明确给出的行为规则，下次 session 直接生效
metadata:
  type: feedback
---

**不写注释**
**Why:** 用户明确说不需要，代码自解释。
**How to apply:** 样例后面不加行尾注释，函数内不加说明注释；docstring 只保留题目描述块。

**不 import 标准库**
**Why:** 用户希望算法逻辑完全手写，体现实现细节。
**How to apply:** 写算法题时不使用任何 import，包括 fractions、random、math 等。

**测试用例要有难度**
**Why:** 简单用例没有意义，用户需要能覆盖边界和反直觉情况的样例。
**How to apply:** 优先构造答案在中间、首尾有多余、大规模、顺序复杂等难用例；删掉过于显而易见的简单用例。

**代码要体现算法结构**（如 DP 状态转移）
**Why:** 直接写结论公式（如求和）不能体现解题思路。
**How to apply:** DP 题要显式写出 dp 数组和转移方程，不能用一行 sum/推导式替代。

**Git 标准流程**
**Why:** 用户希望养成规范的分支管理习惯。
**How to apply:** 新题目在 `ianding_dev`（或专用 feature branch）上开发 → push → 开 PR → merge 进 master；不直接在 master 上 commit。

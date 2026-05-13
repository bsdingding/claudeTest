# 工作规范

## PR 流程
新功能/题目在 feature branch（如 `ianding_cld`）开发，push 后创建 PR 合入 `master`。

## 代码规范
- 不使用任何 import
- 不写注释（docstring 题目描述除外）
- DP 题必须显式写出 dp 数组和状态转移，不用推导式替代

## 测试用例
优先构造：答案在中间、首尾有多余字符、大规模、顺序复杂等难用例。

---
name: pr-review-hook
description: PR 自动代码审核 hook 的配置和工作原理
metadata:
  type: project
---

**配置：** 每次执行 `gh pr create` 后，自动触发严格代码审核 agent，结果以 `additionalContext` 传回给 Claude 输出给用户。

**Why:** 用户希望每次提 PR 时自动做严格审核，不需要手动触发。

**How to apply:** 这套 hook 已配置好，每次创建 PR 时会自动运行，无需额外操作。审核结果会出现在 Claude 的回复里。

## 文件位置

- Hook 脚本：`.claude/hooks/pr-review.sh`
- 项目 hook 配置：`.claude/settings.json`

## 工作流程

1. Claude 执行 `gh pr create` 创建 PR
2. `PostToolUse` hook 检测到命令包含 `gh pr create`
3. 脚本执行 `git diff master...HEAD` 获取代码改动
4. 调用 `claude -p` 对 diff 做严格审核
5. 结果以 JSON `additionalContext` 返回给 Claude
6. Claude 将审核结论输出给用户

## 审核维度

1. 是否使用了 import（禁止，直接 FAIL）
2. 是否有非 docstring 注释（禁止，直接 FAIL）
3. DP 题是否显式写出 dp 数组和状态转移（不能用推导式，否则 FAIL）
4. 测试用例是否覆盖边界、中间答案、大规模输入等难用例
5. 代码整体质量与正确性

## Hook 输出机制（已验证）

- stdout JSON with `hookSpecificOutput.additionalContext` → 传给 Claude 作为上下文（不显示在 UI）
- stderr → 显示在 UI（exit 0 时不会阻断执行）
- exit 2 + stderr → 显示在 UI 并阻断工具执行

#!/bin/bash
input=$(cat)
command=$(echo "$input" | jq -r '.tool_input.command // ""')

if ! echo "$command" | grep -qE "^\s*gh pr create"; then
  exit 0
fi

diff_output=$(git diff master...HEAD 2>/dev/null)

if [ -z "$diff_output" ]; then
  exit 0
fi

review=$(echo "$diff_output" | claude -p "你是一个严格的算法题代码 reviewer。审核以下 git diff，逐条检查：
1. 是否使用了 import（禁止，直接判 FAIL）
2. 是否有非 docstring 的注释（禁止，直接判 FAIL）
3. DP 题是否显式写出了 dp 数组和状态转移（不能用推导式替代，否则 FAIL）
4. 测试用例是否覆盖了边界情况、中间答案、首尾多余字符、大规模输入等难用例
5. 整体代码质量和正确性

每条给出 PASS / FAIL / N/A，最后给出总结。" 2>/dev/null)

jq -n --arg review "$review" '{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": ("=== PR 自动代码审核结果 ===\n" + $review)
  }
}'

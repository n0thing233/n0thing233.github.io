#https://leetcode.com/problems/longest-valid-parentheses/submissions/
#stack to store index + valid_start_index
#O(n)
#O(n)
from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque()
        n = len(s)
        res = 0
        valid_start_index = 0
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif len(stack) != 0:
                stack.pop()
                if len(stack) == 0:
                    res = max(res, i-valid_start_index+1)
                else:
                    res = max(res, i - stack[-1])
            else:
                valid_start_index = i+1
        return res

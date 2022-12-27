"""
https://leetcode.com/problems/valid-parentheses/
"""

class Solution(object):
    def isValid(s: str) -> bool:
        if s is None or len(s) == 0:
            return False
        stack = []
        symbols = { "(" : ")", "[": "]", "{":"}" }

        for brackets in s:
            if brackets in symbols:
                stack.append(brackets)
            elif len(stack)==0 or symbols[ stack.pop() ] != brackets:
                return False
        return len(stack) == 0


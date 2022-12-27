"""
https://leetcode.com/problems/reverse-integer/description/
"""

class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))
        z = y[::-1]
        out = int(z)
        if out >= 2** 31 -1 or out <= -2** 31:
            return 0
        elif x < 0:
            return -1 * out
        else:
            return out
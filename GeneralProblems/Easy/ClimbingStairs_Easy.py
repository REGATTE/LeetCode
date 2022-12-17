"""
https://leetcode.com/problems/climbing-stairs/description/
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1, 2]
        f.extend(f[i-1] + f[i-2] for i in range(2, n))
        return f[n-1]
"""
https://leetcode.com/problems/sqrtx/description/
"""

from math import *
class Solution:
    def mySqrt(self, x: int) -> int:
        a = math.sqrt(x)
        output = math.trunc(a)
        return output
        
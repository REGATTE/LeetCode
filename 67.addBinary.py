"""
https://leetcode.com/problems/add-binary/
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b,2)
        return f'{sum:b}'
        
"""
https://leetcode.com/problems/palindrome-number/description/
"""

class Solution:
    def isPalindrome(self, x: int):
        x = str(x)
        if (x == x[::-1]):
            return True


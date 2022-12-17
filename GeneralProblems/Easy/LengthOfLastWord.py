"""
https://leetcode.com/problems/length-of-last-word/description/
"""

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])
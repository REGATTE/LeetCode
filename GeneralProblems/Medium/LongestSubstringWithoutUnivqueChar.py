"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        
        start, end, maxLength = 0, 0, 0

        unique_value = set()

        while end < len(s):
            if s[end] not in unique_value:
                unique_value.add(s[end])
                end += 1
                maxLength = max(maxLength, len(unique_value))
            else:
                unique_value.remove(s[start])
                start+=1
        return maxLength
"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""

class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        # take length of both words
        lengthOfWord = len(haystack)
        lengthOfNeedle = len(needle)

        # check through length of words
        for i in range(lengthOfWord - lengthOfNeedle + 1):
            # check from i, if next length of word is equal to the needle, else i+=1
            if haystack[i:i + lengthOfNeedle] == needle:
                return i
        else -1


"""
=================
"""


class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
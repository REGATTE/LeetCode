"""
https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan&id=level-1
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]
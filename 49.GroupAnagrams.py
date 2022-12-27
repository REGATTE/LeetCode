"""
https://leetcode.com/problems/group-anagrams/description/
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        output = collections.defaultdict(list)
        for value in strs:
            data = ''.join(sorted(value))
            output[data].append(value)
        return output.values()

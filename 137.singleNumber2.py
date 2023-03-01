"""
https://leetcode.com/problems/single-number/submissions/906998656/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number_list = []
        out = 0
        for num in nums:
            out = out ^ num
        return out
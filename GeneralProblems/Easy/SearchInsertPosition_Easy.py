"""
https://leetcode.com/problems/search-insert-position/
"""

class Solution:
    def searchInsert(self, nums, target):
        if nums is None or len(nums) == 0: return 0
        for i, n in enumerate(nums):
            if (n >= target):
                return i
        return len(nums)
        
        


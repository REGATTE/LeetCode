"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftIndex = bisect.bisect_left(nums, target)
        if leftIndex == len(nums) or nums[leftIndex] != target:
            return [-1, -1]
        rightIndex = bisect.bisect_right(nums, target) - 1
        return leftIndex, rightIndex
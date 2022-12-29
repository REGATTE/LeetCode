"""
https://leetcode.com/problems/binary-search/description/?envType=study-plan&id=level-1
"""

## Main Solution - BINARY SEARCH
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

## Other Solution [FASTER]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, val in enumerate(nums):
            if val == target:
                return i
        return -1
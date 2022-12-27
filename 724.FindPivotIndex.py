"""
https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumValues = sum(nums)
        checkValue = 0

        for i, num in enumerate(nums):
            if checkValue == sumValues - checkValue - num:
                return i
            checkValue += num
        return -1


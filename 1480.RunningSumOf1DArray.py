"""
https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 1:
            return nums
        """
        newList = []
        for i in range(len(nums)):
            newList.append(sum(nums[:i+1]))
        return newList
        """
        return [sum(nums[:i+1]) for i in range(len(nums))]

"""
==================================================================
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums

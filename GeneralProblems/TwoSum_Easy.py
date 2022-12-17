"""
https://leetcode.com/problems/two-sum/
"""

class Solution(object):
    def twoSum(self, nums, target):
        # define a empty dictionary to take in index and value
        output_value = {}
        # index = i, value = num
        for i, num in enumerate(nums):
            if target - num in output_value:
                return [nums.index(target - num), i]
            output_value[num] = i
        return []

"""
Time = O(n)
Space = O(n) 
"""
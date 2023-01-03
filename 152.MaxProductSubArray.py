"""
https://leetcode.com/problems/maximum-product-subarray/description/
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = nums[0]
        minimum = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            minValue = minimum * nums[i]
            maxValue = maximum * nums[i]
            minimum = min(nums[i], minValue, maxValue)
            maximum = max(nums[i], minValue, maxValue)
            output = max(output, maximum)
        return output
    
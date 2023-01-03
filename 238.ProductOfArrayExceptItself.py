"""
https://leetcode.com/problems/product-of-array-except-self/description/
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before_number = [1] * n
        after_number = [1] * n

        for i in range(1, n):
            before_number[i] = before_number[i-1] * nums[i-1]
        for i in reversed(range(n-1)):
            after_number[i] = after_number[i+1] * nums[i+1]
        return [before_number[i] * after_number[i] for i in range(n)]
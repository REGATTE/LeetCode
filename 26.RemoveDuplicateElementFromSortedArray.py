"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def removeDuplicates(self, nums):
        length_original = len(nums)
        sorted_list = []
        count = 0

        if len(nums) < 2:
            return nums

        for i in range(length_original):
            if nums[i] not in sorted_list:
                sorted_list.append(nums[i])
                nums[count] = nums[i]
                count += 1

        return count

nums = [0,0,1,1,1,2,2,3,3,4]


Solution.removeDuplicates(nums)
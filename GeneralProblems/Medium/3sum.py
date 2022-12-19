"""
https://leetcode.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        output = []

        for pointer1 in range(len(nums) - 2):
            if pointer1 > 0 and nums[pointer1] == nums[pointer1 -1]:
                continue
            pointer2 = pointer1 + 1
            pointer3 = len(nums) - 1
            summ = nums[pointer1] + nums[pointer2] + nums[pointer3]
            if summ == 0:
                output.append((nums[pointer1], nums[pointer2], nums[pointer3]))
                pointer2 += 1
                pointer3 -= 1
                while pointer3 > pointer2 and nums[pointer2] == nums[pointer2 - 1]:
                    pointer2 += 1
                while pointer3 > pointer2 and nums[pointer3] == nums[pointer3 + 1]:
                    pointer3 -= 1
            elif summ < 0:
                pointer2+=1
            else:
                pointer3-=1
            pointer1 += 1
        return output
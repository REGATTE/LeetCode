"""
https://leetcode.com/problems/sort-colors/
"""

class Solution:
  def sortColors(self, nums: List[int]) -> None:
    x, y = 0, 0  # Next 0 should be put in l
    r = len(nums) - 1  # Next 2 should be put in r

    while x <= r:
        if nums[x] == 0:
            nums[x], nums[y] = nums[y], nums[x]
            x += 1
            y += 1
        elif nums[x] == 1:
            x += 1
        else:
            # We may swap a 0 to index i, but we're still not sure whether
            # this 0 is put in the correct index, so we can't move pointer i
            nums[x], nums[r] = nums[r], nums[x]
            r -= 1

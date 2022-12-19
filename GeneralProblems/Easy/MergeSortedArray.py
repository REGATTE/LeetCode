"""
https://leetcode.com/problems/merge-sorted-array/description/
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1 = m - 1
        index_2 = n - 1
        index_to_append = m + n - 1

        while index_2 >= 0:
            if index_1 >= 0 and nums1[index_1] > nums2[index_2]:
                nums1[index_to_append] = nums1[index_1]
                index_to_append -= 1
                index_1 -= 1
            else:
                nums1[index_to_append] = nums2[index_2]
                index_to_append -= 1
                index_2 -= 1
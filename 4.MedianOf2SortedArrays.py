"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        new_list= nums1 + nums2
        n = len(new_list)
        s = sorted(new_list)
        return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None
"""
https://leetcode.com/problems/merge-two-sorted-lists/

given list is a linked list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode(0)
        head = new_list

        while (l1 and l2):
            if l1.val < l2.val:
                new_list.next = l1
                l1 =l1.next
            else:
                new_list.next = l2
                l2 =l2.next
            new_list = new_list.next
        new_list.next = l1 or l2
        return head.next
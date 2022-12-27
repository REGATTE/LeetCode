"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer_1 = head
        pointer_2 = pointer_1

        for _ in range(n):
            pointer_1 = pointer_1.next
        
        if not pointer_1:
            return pointer_2.next
        
        while pointer_1.next:

            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
        
        pointer_2.next = pointer_2.next.next
        return head
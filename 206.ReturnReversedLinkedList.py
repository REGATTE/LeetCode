"""
https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan&id=level-1
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        """
        2 pointer approach

        prevNode is set to None, currNode is set to head

        define nextNode to currNode.next and shift currNode.next to prev i.e.,e None.
        then pun prev to curr. i.e., in other words, putting currNode.next = currNode

        then put currNode to next i.e., currNode = currNode.net before swap
        """
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
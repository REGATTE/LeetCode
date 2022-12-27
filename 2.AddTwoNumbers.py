"""
https://leetcode.com/problems/add-two-numbers/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, temp = None, None
        carry = 0
        while l1 or l2:
            sum_value = carry
            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next
            
            node = ListNode(sum_value % 10)
            carry = sum_value // 10
            if temp is None:
                head = node
                temp = head
            # for any other node
            else:
                temp.next = node
                temp = temp.next
        if carry > 0:
            temp.next = ListNode(carry)
        return head

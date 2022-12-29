"""
https://leetcode.com/problems/middle-of-the-linked-list/description/
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        midleNode()
        - takes the head of linkedList in
        - pointer_1 moves forward by 1 step
        - pointer_2 moves forward by 2 steps
        - at the end, when pointer_2 is None and pointer_2.next is None, pointer1 will point to the midle of the node
        - return pointer_1
        """
        def midleNode(head):
            pointer_1 = head
            pointer_2 = head
            while pointer_2 is not None and pointer_2.next is not None:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next.next
            return pointer_1
        return midleNode(head)
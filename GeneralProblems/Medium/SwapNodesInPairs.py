"""
https://leetcode.com/problems/swap-nodes-in-pairs/
"""

class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to be before head
        dummyNode = ListNode(0)

        # create a copy of the dummy nodde
        currentNode = dummyNode

        #point current node to head
        currentNode.next = head

        # while loop to swap
        while currentNode.next is not None and currentNode.next.next is not None:

            # define first and second node
            firstNode = currentNode.next
            secondNode = currentNode.next.next

            # point first node to second node next to follow after swap
            firstNode.next = secondNode.next

            # swap
            currentNode.next, currentNode.next.next = secondNode, firstNode

            # shift current node forward
            currentNode = currentNode.next.next
        
        return dummyNode.next


"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        treeQueue = collections.deque([root])
        output = []
        LeftToRight = True

        while treeQueue:
            treeLevel = []
            for _ in range(len(treeQueue)):
                if LeftToRight:
                    node = treeQueue.popleft()
                    treeLevel.append(node.val)
                    if node.left: treeQueue.append(node.left)
                    if node.right: treeQueue.append(node.right)
                else:
                    node = treeQueue.pop()
                    treeLevel.append(node.val)
                    if node.right: treeQueue.appendleft(node.right)
                    if node.left: treeQueue.appendleft(node.left)
            output.append(treeLevel)
            LeftToRight = not LeftToRight
        return output
            
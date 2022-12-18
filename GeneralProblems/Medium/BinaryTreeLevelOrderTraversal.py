"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue_tree = collections.deque([root])
        output = []

        while queue_tree:
            treeLevel = []
            for _ in range(len(queue_tree)):
                node = queue_tree.popleft()
                treeLevel.append(node.val)
                if node.left: queue_tree.append(node.left)
                if node.right: queue_tree.append(node.right)
            output.append(treeLevel)
        return output

"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        # general case
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        return max(leftDepth, rightDepth) + 1
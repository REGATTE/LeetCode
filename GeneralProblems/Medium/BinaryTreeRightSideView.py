"""
https://leetcode.com/problems/binary-tree-right-side-view/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        output = []
        value = collections.deque([root])

        while value:
            size = len(value)
            for i in range(size):
                root = value.popleft()
                if i == size - 1:
                    output.append(root.val)
                if root.left:
                    value.append(root.left)
                if root.right:
                    value.append(root.right)
        return output
                


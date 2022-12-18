"""
https://leetcode.com/problems/symmetric-tree/
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetry(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p or not q:
                return p == q
            return (p.val == q.val) and check_symmetry(p.left, q.right) and check_symmetry(p.right, q.left)
        return check_symmetry(root, root)
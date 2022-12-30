"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/?envType=study-plan&id=level-1
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return root

        ans = []
        if root.children:
            for node in root.children:
                ans.extend(self.preorder(node))
        return [root.val] + ans

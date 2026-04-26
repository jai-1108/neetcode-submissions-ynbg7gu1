# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0 
            right_h = dfs(node.right)
            left_h = dfs(node.left)
            self.diameter = max(self.diameter, left_h + right_h)
            return 1 + max(left_h, right_h)
        dfs(root)
        return self.diameter
        
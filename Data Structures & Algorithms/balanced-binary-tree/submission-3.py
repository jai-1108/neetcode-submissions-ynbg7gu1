# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
                return -1
            else:
                return 1+max(left_h,right_h)
        if dfs(root) != -1:
            return True
        else:
            return False
        

            
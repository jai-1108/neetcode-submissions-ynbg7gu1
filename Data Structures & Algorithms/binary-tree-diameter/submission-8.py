# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        left_h = self.maxheight(root.left)
        right_h = self.maxheight(root.right)
        diameter = left_h + right_h
        ans = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(ans, diameter)
        
    def maxheight(self, root):
        if not root:
            return 0
        return 1 + max(self.maxheight(root.left), self.maxheight(root.right))
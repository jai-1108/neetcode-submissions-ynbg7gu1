# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        if small > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if large < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        


        
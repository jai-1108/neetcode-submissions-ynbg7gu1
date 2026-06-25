# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append([root, root.val])
        count = 0
        while q:
            qlen = len(q)
            for _ in range(qlen):
                node, max_so_far = q.popleft()
                if node.val >= max_so_far:
                    count += 1
                max_so_far = max(max_so_far, node.val)
                if node.left:
                    q.append([node.left, max_so_far])
                if node.right:
                    q.append([node.right, max_so_far])
        return count

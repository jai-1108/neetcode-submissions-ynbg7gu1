class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)]
        res = n
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                parent[root1] = root2
                return True
            return False
        for u,v in edges:
            if not union(u,v):
                return [u, v]

        
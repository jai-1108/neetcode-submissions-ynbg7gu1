class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        res = n
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(u,v):
            root1 = find(u)
            root2 = find(v)
            if root1 != root2:
                parent[root1] = root2
                return True
            return False
        
        for u,v in edges:
            if union(u,v):
                res -= 1
        return res
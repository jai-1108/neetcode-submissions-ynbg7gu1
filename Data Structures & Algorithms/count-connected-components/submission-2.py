class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        nodes = [i for i in range(n)]
        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        res = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return 
        for node in nodes:
            if node not in visited:
                dfs(node)
                res += 1
        return res
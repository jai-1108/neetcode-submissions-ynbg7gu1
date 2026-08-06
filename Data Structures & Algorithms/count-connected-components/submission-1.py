class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        nodes = [i for i in range(n)]
        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        res = 0
        visited = set()
        def dfs(node, par):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                dfs(nei, node)
            return 
        par = -1
        for node in nodes:
            if node not in visited:
                dfs(node, par)
                res += 1
        return res
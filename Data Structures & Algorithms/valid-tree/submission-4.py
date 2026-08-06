class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adjList = defaultdict(list)
        for node, nei in edges:
            adjList[node].append(nei)
            adjList[nei].append(node)
        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjList[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(visited) == n

        
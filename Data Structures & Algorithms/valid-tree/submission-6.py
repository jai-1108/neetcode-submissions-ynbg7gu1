class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        nodes = [i for i in range(n)]
        hashmap = defaultdict(list)
        for node, nei in edges:
            hashmap[node].append(nei)
            hashmap[nei].append(node)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in hashmap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        dfs(0, -1)
        return len(visited) == n




        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        nodes = [i for i in range(n)]
        hashmap = defaultdict(list)
        visited = set()
        for node, nei in edges:
            hashmap[node].append(nei)
            hashmap[nei].append(node)
        """
        hashmap = {0: 1,2,3, 1:4}
        """
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
          
        return dfs(0, -1) and len(visited) == n 
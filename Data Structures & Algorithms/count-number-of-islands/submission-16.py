class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] != "1":
                return False
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
            return True
        no_of_islands = 0
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c):
                    no_of_islands += 1
        return no_of_islands



            
        
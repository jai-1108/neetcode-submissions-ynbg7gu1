class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        path = set()
        no_of_islands = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in path or grid[r][c] == "0":
                return
            path.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in path:
                    no_of_islands += 1
                    dfs(r,c)
        return no_of_islands   

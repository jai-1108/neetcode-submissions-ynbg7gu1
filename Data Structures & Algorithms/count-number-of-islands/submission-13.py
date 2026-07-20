class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        no_of_islands = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] == "0" or (nr,nc) in visited:
                        continue
                    q.append((nr,nc))
                    visited.add((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    no_of_islands += 1
        return no_of_islands
        
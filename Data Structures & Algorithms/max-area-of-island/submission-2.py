class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        max_area = 0
        def bfs(r,c,area):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            while q:
                r, c = q.popleft()
                area += 1
                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                        continue      
                    q.append((nr,nc))
                    grid[nr][nc] = 0
            return area

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r,c,0))
        return max_area



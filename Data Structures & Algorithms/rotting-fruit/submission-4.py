class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        timer = 0
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        while q:
            level_size = len(q)
            for _ in range(level_size):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr,nc))
            if q:
                timer += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return timer

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rows = len(grid)
        cols = len(grid[0])
        timer = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        while q:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
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

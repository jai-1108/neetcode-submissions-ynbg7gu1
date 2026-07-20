class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        max_area = 0
        def bfs(r,c,area):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r, c = q.popleft()
                area += 1
                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0 or (nr,nc) in visited:
                        continue      
                    q.append((nr,nc))
                    visited.add((nr,nc))
            return area

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, bfs(r,c,0))
        return max_area



class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                if r == rows-1 or c == cols-1:
                    atlantic.add((r,c))
        def bfs(ocean_set):
            q = deque(ocean_set)
            while q:
                r,c  = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr,nc) in ocean_set or heights[nr][nc] < heights[r][c]:
                        continue
                    ocean_set.add((nr,nc))
                    q.append((nr,nc))
        bfs(pacific)
        bfs(atlantic)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
                 

        
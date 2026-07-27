class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        pacific = set()
        atlantic = set()
        
        rows = len(heights)
        cols = len(heights[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                if r == (rows - 1) or c == (cols - 1):
                    atlantic.add((r,c))
        
        def bfs(ocean_set):
            q = deque(list(ocean_set))
            visited = set(ocean_set)
            while q:
                r, c  = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr,nc))
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
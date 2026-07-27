class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r,c,ocean_set,prev_elem):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in ocean_set or heights[r][c] < prev_elem:
                return
            ocean_set.add((r,c))
            prev_elem = heights[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr,nc,ocean_set,prev_elem)

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr,nc)
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
            

        
        
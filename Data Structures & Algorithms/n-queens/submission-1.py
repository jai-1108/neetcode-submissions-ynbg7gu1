class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        left_diag = set()
        right_diag = set()

        res = []
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r+c) in right_diag or (r-c) in left_diag:
                    continue
                cols.add(c)
                left_diag.add(r-c)
                right_diag.add(r+c)
                board[r][c] = "Q"
                backtrack(r+1)
                cols.remove(c)
                left_diag.remove(r-c)
                right_diag.remove(r+c)
                board[r][c] = "."
        backtrack(0)
        return res
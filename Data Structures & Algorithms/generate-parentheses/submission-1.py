class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, open, close):
            if len(path) == 2*n:
                res.append("".join(path))
                return
            if open < n:
                path.append("(")
                open += 1
                backtrack(path, open, close)
                path.pop()
                open -= 1
            if close < open:
                path.append(")")
                close += 1
                backtrack(path, open, close)
                path.pop()
                close -= 1
        backtrack([], 0, 0)
        return res
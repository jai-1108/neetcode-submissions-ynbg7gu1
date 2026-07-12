class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(string, open, close):
            if len(string) == 2*n:
                res.append("".join(string))
                return
            if open < n:
                string.append("(")
                open += 1
                backtrack(string, open, close)
                string.pop()
                open -= 1
            if close < open:
                string.append(")")
                close += 1
                backtrack(string, open, close)
                string.pop()
                close -= 1
        backtrack([],0,0)
        return res

        
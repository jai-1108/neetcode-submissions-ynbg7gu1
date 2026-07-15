class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        path = []
        if not digits:
            return []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(path))
                return
            for j in range(len(hashmap[digits[i]])):
                path.append(hashmap[digits[i]][j])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return res

        
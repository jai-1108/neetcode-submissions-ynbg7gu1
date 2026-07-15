class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashmap = defaultdict(list)
        hashmap["2"] = ["a","b","c"]
        hashmap["3"] = ["d","e","f"]
        hashmap["4"] = ["g","h","i"]
        hashmap["5"] = ["j","k","l"]
        hashmap["6"] = ["m","n","o"]
        hashmap["7"] = ["p","q","r","s"]
        hashmap["8"] = ["t","u","v"]
        hashmap["9"] = ["w","x","y","z"]
        path = []
        if not digits:
            return []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(path.copy()))
                return
            for j in range(len(hashmap[digits[i]])):
                path.append(hashmap[digits[i]][j])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return res

        
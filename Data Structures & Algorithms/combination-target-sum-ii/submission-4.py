class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        self.total = 0
        def dfs(i):
            if self.total == target:
                res.append(path.copy())
                return
            if self.total > target or i == len(candidates):
                return
            path.append(candidates[i])
            self.total += candidates[i]
            dfs(i+1)
            path.pop()
            self.total -= candidates[i]
            next_i = i+1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            dfs(next_i)
        dfs(0)
        return res
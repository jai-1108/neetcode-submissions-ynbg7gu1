class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        def dfs(i, total, target):
            if total == target:
                res.append(path.copy())
                return
            if total > target or i == len(candidates):
                return
            total += candidates[i]
            path.append(candidates[i])
            dfs(i+1, total, target)
            total -= candidates[i]
            path.pop()
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            dfs(next_i, total, target)
        dfs(0, 0, target)
        return res
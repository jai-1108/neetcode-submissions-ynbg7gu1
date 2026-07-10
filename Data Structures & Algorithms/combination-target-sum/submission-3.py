class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i, total, target):
            if total > target or i == len(nums):
                return
            if total == target:
                res.append(path.copy())
                return
            total += nums[i]
            path.append(nums[i])
            dfs(i, total, target)
            total -= nums[i]
            path.pop()
            dfs(i+1, total, target)
        dfs(0, 0, target)
        return res
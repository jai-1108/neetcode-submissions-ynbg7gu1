class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i, total, target):
            if i == len(nums) or total > target:
                return
            if total == target:
                res.append(path.copy())
                return
            path.append(nums[i])
            total += nums[i]
            dfs(i, total, target)
            path.pop()
            total -= nums[i]
            dfs(i+1, total, target)
        dfs(0, 0, target)
        return res
        
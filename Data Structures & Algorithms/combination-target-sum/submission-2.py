class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combo = []
        self.total = 0
        res = []
        def dfs(i):
            if self.total == target:
                res.append(combo.copy())
                return  
            if self.total > target:
                return
            if i == len(nums):
                return
            self.total += nums[i]
            combo.append(nums[i])
            dfs(i)
            self.total -= nums[i]
            combo.pop()
            dfs(i+1)
        dfs(0)
        return res
            

        
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.robber(nums[:n-1]), self.robber(nums[1:]))

    def robber(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        prev1 = max(nums[0], nums[1])
        prev2 = nums[0]
        for i in range(2, len(nums)):
            current = max(nums[i]+prev2, prev1)
            prev2 = prev1
            prev1 = current
        return current
        
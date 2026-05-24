class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,4,6]
        prefix = [1,1,1,1]
        postfix = [1,1,1,1]
        
        prefix = [1,1,2,8]
        postfix = [48,24,6,1]
        res = [48,24,12,8]
        """
        prefix = [1]*(len(nums))
        postfix = [1]*(len(nums))
        res = [1]*(len(nums))
        for i in range(1,len(nums)):
            prefix[i] = nums[i-1]*prefix[i-1]
        for j in range(len(nums)-2,-1,-1):
            postfix[j] *= nums[j+1]*postfix[j+1]
        for k in range(len(nums)):
            res[k] = prefix[k]*postfix[k]
        return res
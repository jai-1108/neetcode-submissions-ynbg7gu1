class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i,a in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = len(nums)-1
                while l<r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum>target:
                        r-=1
                    elif sum<target:
                        l+=1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        while r>l and nums[r] == nums[r+1]:
                            r-=1
        return res

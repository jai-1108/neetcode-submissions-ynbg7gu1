class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        """
        mid = 2
        nums[mid] = 5,  nums[l] = 3, l = mid+1, l=3
        mid = 4, nums[mid] = 1, 
        """
        if nums[l] < nums[r]:
            return nums[l]
        
        while l<r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l  = mid + 1
            else:
                r = mid
        return nums[l]


        
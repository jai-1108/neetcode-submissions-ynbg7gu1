class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l<r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        l = 0
        r = len(nums) - 1
        if self.binary_search(pivot, r, target, nums) != -1:
            return self.binary_search(pivot, r, target, nums)
        else:
             return self.binary_search(l, pivot-1, target, nums)
            
    def binary_search(self, left: int, right: int, tar: int, array: List[int]):
        while left <= right:
            mid = (left + right) // 2
            if array[mid] > tar:
                right = mid - 1
            elif array[mid] < tar:
                left = mid + 1
            else:
                return mid
        return -1

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for n in nums2:
            nums1.append(n)
        nums1.sort()
        length = len(nums1)
        if length % 2 != 0:
            return nums1[length//2]
        else:
            return (nums1[(length//2)-1] + nums1[(length//2)])/2
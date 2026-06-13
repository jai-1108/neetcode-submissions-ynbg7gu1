class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        for n in nums1:
            merged.append(n)
        for n in nums2:
            merged.append(n)
        merged.sort()
        l = len(merged)
        if l % 2 == 0:
            return (merged[(l//2)-1] + merged[l//2])/2
        else:
            return merged[l//2]

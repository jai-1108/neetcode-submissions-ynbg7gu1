class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        p1 = 0
        p2 = 0
        i = 0
        merged = [0]*(m+n)
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                merged[i] = nums1[p1]
                p1 += 1
                i += 1
            else:
                merged[i] = nums2[p2]
                p2 += 1
                i += 1
        while p1 < m:
            merged[i] = nums1[p1]
            p1 += 1
            i += 1
        while p2 < n:
            merged[i] = nums2[p2]
            p2 += 1
            i += 1
        l = len(merged)
        if l % 2 == 0:
            return (merged[(l//2)-1] + merged[l//2])/2
        else:
            return merged[l//2]

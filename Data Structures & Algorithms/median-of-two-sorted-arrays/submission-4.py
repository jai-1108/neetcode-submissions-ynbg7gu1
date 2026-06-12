class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = 0
        l2 = 0
        nums3 = [0]*(len(nums1) + len(nums2))
        i = 0
        while l1<len(nums1) and l2<len(nums2):
            if nums1[l1] < nums2[l2]:
                nums3[i] = nums1[l1]
                i += 1
                l1 +=1
            else:
                nums3[i] = nums2[l2]
                i += 1
                l2 += 1
        while l1 < len(nums1):
            nums3[i] = nums1[l1]
            i += 1
            l1 += 1
        while l2 < len(nums2):
            nums3[i] = nums2[l2]
            i += 1
            l2 += 1
        l = len(nums3)
        if l % 2 != 0:
            return float(nums3[l//2])
        else:
            return (nums3[(l//2)-1]+nums3[l//2])/2.0
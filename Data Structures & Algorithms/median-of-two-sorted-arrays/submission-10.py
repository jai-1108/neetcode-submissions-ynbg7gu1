class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            A,B = B,A
        l = 0
        r = len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        while True:
            i = (l+r)//2
            j = half - (i+1) - 1
            leftA = A[i] if i>=0 else float("-inf") #rightmost element of left array
            leftB = B[j] if j>=0 else float("-inf") #rightmost element of left array
            rightA = A[i+1] if (i+1) < len(A) else float("inf") #leftmost element of right array
            rightB = B[j+1] if (j+1) < len(B) else float("inf") #leftmost element of right array

            if leftA > rightB:
                r = i - 1
            elif rightA < leftB:
                l = i + 1
            else:
                if total % 2:
                    return min(rightA, rightB)
                else:
                    median = (max(leftA, leftB) + min(rightA, rightB))/2
                    return median



class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftmax = 0
        rightmax = 0
        area = 0
        while l<r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])
            if leftmax<rightmax:
                area += leftmax - height[l]
                l+=1
                
            else:
                area += rightmax - height[r]
                r-=1
        return area
        
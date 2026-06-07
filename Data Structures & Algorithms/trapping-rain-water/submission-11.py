class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i-1], height[i-1])
        rightmax= [0]*len(height)
        for i in range(len(height)-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i+1])
        res = 0
        area = 0
        for i in range(len(height)):
            area = min(leftmax[i], rightmax[i]) - height[i] 
            res += area if area > 0 else 0
        return res

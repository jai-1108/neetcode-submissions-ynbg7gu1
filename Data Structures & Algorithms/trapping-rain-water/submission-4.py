class Solution:
    def trap(self, height: List[int]) -> int:
        """
        leftmax = [0,0,2,2,3,3,3,3,3,3,3] #max element seen so far before ith index from left
        rightmax = [3,3,3,3,3,3,3,3,2,1,0] #max element seen so far before ith index from right
        area += if (min(leftmax[i],rightmax[i])-height[i]) > 0 
                then (min(leftmax[i],rightmax[i])-height[i]) else 0
        area = [0+0+2+0+2+3+2+0+0+0]

        """
        leftmax = [0]*len(height)
        for i in range(1,len(height)):
            leftmax[i] = max(height[i-1], leftmax[i-1])
        rightmax = [0]*len(height)
        for i in range(len(height)-2,-1,-1):
            rightmax[i] = max(height[i+1], rightmax[i+1])
        area = 0
        for i in range(len(height)):
            area += min(leftmax[i],rightmax[i]) - height[i] if (min(leftmax[i],rightmax[i]) - height[i]) > 0 else 0
        return area

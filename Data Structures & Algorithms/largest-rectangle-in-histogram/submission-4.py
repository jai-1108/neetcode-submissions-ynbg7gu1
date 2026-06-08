class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        stack = 
        """
        max_area = 0
        for i in range(len(heights)):
            l = i
            r = i
            while l >= 0 and heights[l] >= heights[i]:
                l -= 1
            while r<len(heights) and heights[r] >= heights[i]:
                r += 1
            l += 1
            r -= 1
            width = r - l + 1
            length = heights[i]
            area = length * width
            max_area = max(max_area, area)
        return max_area

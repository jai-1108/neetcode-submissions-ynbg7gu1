class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            left = i
            right = i 
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            while right < len(heights) and heights[right] >= heights[i]:
                right += 1
            left += 1
            right -= 1
            width = right - left + 1
            area = heights[i] * width
            max_area = max(area, max_area)
        return max_area
        
        
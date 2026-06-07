class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n):
            height = heights[i]
            left = i
            while left >= 0 and heights[left] >= height:
                left -= 1
            right = i+1
            while right < n and heights[right] >= height:
                right += 1
            left += 1
            right -= 1
            area = height * (right - left + 1)
            max_area = max(max_area, area)
        return max_area

        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        """
        l = 0, 1
        r = 7, 6
        area = 7*1 = 7
        res = 7

        l = 1, 7
        r = 7, 6
        area = 6*6 = 36
        res = 36


        """
        l = 0
        r = len(heights) - 1
        while l<r:
            length = min(heights[l],heights[r])
            breadth = r-l
            area = length * breadth
            res = max(res, area)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return res
        
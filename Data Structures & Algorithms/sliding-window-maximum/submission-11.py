from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        res = []
        window = [0]
        window = [1]
        window = [1,2]

        """
        res = []
        window = deque()
        l = 0
        r = 0
        while r<len(nums):
            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)
            if r-l+1 == k:
                res.append(nums[window[0]])
                l += 1
            if l > window[0]:
                window.popleft()
            r += 1

        return res




            
            
        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        """
        q = []
        res = []
        l = 0
        r = 0, q = [0]
        r = 1, q = [1]
        r = 2, q = [1,2], r-l+1=3 == k:
            res = [2]
            l = 1
        r = 3, q = [1,2,3], r-l+1=3 == k
            res = [2,2]
            l = 2
        q[0] = 1 < l
            q = [2,3] 
        
    
        """
        res = []
        l = 0
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if (r-l+1) == k:
                res.append(nums[q[0]])
                l += 1
            if l > q[0]:
                q.popleft()
        return res

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = float("inf")
        while l<=r:
            mid = (l+r) // 2
            total_time = 0
            for p in piles:
                time = math.ceil(p/mid)
                total_time += time
            if total_time > h:
                l = mid + 1
            else:
                ans = min(ans, mid)
                r = mid - 1
        return ans
            
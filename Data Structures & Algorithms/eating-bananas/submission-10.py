class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = float("inf")
        while l<=r:
            mid = l + (r-l)//2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/mid)
            if total_time > h:
                l = mid + 1
            else:
                ans = mid
                res = min(ans,mid)
                r = mid - 1
        return ans

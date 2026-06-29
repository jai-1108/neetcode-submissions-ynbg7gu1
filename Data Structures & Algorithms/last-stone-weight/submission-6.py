class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        maxheap = []
        for n in stones:
            maxheap.append(-n)
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            a = -heapq.heappop(maxheap)
            b = -heapq.heappop(maxheap)
            if (a-b) != 0:
                heapq.heappush(maxheap, -(a-b))
            else:
                heapq.heappush(maxheap, 0)
        return -maxheap[0]
        
        
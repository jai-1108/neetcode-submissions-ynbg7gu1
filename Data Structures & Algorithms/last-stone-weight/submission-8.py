class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = -1*heapq.heappop(maxHeap)
            stone2 = -1*heapq.heappop(maxHeap)
            if stone1 != stone2:
                stone3 = -1*(stone1 - stone2)
                heapq.heappush(maxHeap, stone3)
        return 0 if not maxHeap else -maxHeap[0]

        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            a = -heapq.heappop(maxHeap)
            b = -heapq.heappop(maxHeap)
            if a != b:
                heapq.heappush(maxHeap, -(a-b))
            else:
                heapq.heappush(maxHeap, 0)
        return -maxHeap[0]


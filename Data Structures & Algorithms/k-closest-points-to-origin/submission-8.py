class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x,y in points:
            dist = x**2 + y**2
            maxHeap.append([-dist, [x, y]])
        heapq.heapify(maxHeap)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        res = [item[1] for item in maxHeap]
        return res

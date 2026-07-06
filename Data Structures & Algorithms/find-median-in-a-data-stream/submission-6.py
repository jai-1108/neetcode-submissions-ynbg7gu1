class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        if self.minheap and self.maxheap and -(self.maxheap[0]) >= self.minheap[0]:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -val)
        if len(self.minheap) - len(self.maxheap) > 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)
        if len(self.maxheap) - len(self.minheap) > 1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -val)

    def findMedian(self) -> float:
        l1 = len(self.maxheap) 
        l2 = len(self.minheap)
        if l1 > l2:
            return -(self.maxheap[0])
        if l2 > l1:
            return self.minheap[0]
        else:
            median = (-(self.maxheap[0]) + self.minheap[0])/2.0
            return median
        
        
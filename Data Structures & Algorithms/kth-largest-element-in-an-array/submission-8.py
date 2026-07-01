class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [n for n in nums]
        heapq.heapify(minheap)
        while len(minheap) > k:
            heapq.heappop(minheap)
        return minheap[0]
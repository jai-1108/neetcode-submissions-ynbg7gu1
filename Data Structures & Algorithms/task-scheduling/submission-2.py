class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = {}
        for t in tasks:
            task_counts[t] = 1 + task_counts.get(t,0)
        maxHeap = []
        for val in task_counts.values():
            maxHeap.append(-val)
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                cooldown = time + n
                if freq < 0:
                    q.append([freq, cooldown])
            if q and time == q[0][1]:
                task = q.popleft()
                heapq.heappush(maxHeap, task[0])
        return time
            


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        freq = {1:1, 2:2, 3:3}
        sort.keys = [3,2,1]
        res = [3], k=1
        res = [3,2], k=0

        """
        freq = {}
        res = []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        buckets = []
        for _ in range(len(nums)+1):
            buckets.append([])
        for num, cnt in freq.items():
            buckets[cnt].append(num)
        for i in range(len(buckets)-1, 0, -1):
            for elem in buckets[i]:
                res.append(elem)
                k-=1
                if k==0:
                    return res
        return 
            

        

        

        
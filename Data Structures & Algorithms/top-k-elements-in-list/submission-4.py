class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        freq = {1:1, 2:2, 3:3}
        sort.keys = [3,2,1]
        res = [3], k=1
        res = [3,2], k=0

        """
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        sorted_keys = sorted(freq, key = lambda x: freq[x], reverse = True)
        return sorted_keys[:k]
        

        
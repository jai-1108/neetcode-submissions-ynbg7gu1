class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        numset = set
        """
        longest = 0
        numset = set(nums)
        for num in nums:
            length = 1
            if num-1 in numset:
                continue
            else:
                while num+1 in numset:
                    length += 1
                    num += 1
            longest = max(length, longest)
            
        return longest
        
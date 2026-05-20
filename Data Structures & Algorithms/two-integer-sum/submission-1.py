class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        hashmap = val -> index
        hashmap = {6:0, 5:1, }
        """
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target-n
            if n in hashmap:
                return [hashmap[n],i]
            hashmap[diff] = i
        return
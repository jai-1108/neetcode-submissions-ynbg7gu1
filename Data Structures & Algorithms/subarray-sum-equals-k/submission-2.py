class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        prefix_counts = {0:1}
        current_sum = 0
        for num in nums:
            current_sum += num
            target = current_sum - k
            if target in prefix_counts:
                count += prefix_counts[target]
            prefix_counts[current_sum] = 1 + prefix_counts.get(current_sum,0)
        return count




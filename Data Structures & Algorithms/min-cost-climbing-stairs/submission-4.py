class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        one = cost[0]
        two = cost[1]
        for i in range(2, n):
            current = min(one, two) + cost[i]
            one = two
            two = current
        return min(one, two)
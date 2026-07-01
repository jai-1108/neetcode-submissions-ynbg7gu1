class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        res = [0,0,0,0,0,0,0]
        stack = [0]
        while temperatures[i] > temperatures[stack[-1]]:
            stack = []
            1-0
            res[0] = 1
            stack = [1]
        stack = [1,2]
        stack = [1]
        res[2] = 3-2
        res = [1,0,1,0,0,0,0]
        stack = [1,3]
        stack = [1,3,4]
        stack = [1,3]
        res[4] = 5-4 = 1
        stack = [1]
        res[3] = 5-3 = 2
        stack = []
        res[1] = 5-1 = 4
        res = [1,4,1,2,1,0,0]
        stack = [5]

        """
        res = [0]*len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)
        return res



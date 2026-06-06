class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position, speed = [(1,3),(4,2)]
        [(4,2),(1,3)]
        time = [3,3], time = target-p / s
        if time and time[-1] >= time[i]:
            no_of_fleets += 1
        return no_of_fleets
        """
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        stack = []
        no_of_fleets = 0
        for p, s in cars:
            distance = target - p
            stack.append(distance/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


class MedianFinder:

    def __init__(self):
        self.array = []
        

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array.sort()

    def findMedian(self) -> float:
        n = len(self.array)
        if n == 1:
            return self.array[0]
        if n%2:
            return float(self.array[n//2])
        else:
            median = (self.array[n//2] + self.array[(n//2)-1])/2.0
            return median
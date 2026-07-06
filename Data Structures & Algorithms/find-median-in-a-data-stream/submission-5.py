class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array.sort()
        

    def findMedian(self) -> float:
        l = len(self.array)
        if l % 2:
            return self.array[l//2]
        else:
            median = (self.array[l//2] + self.array[l//2 - 1])/2.0
            return median
        
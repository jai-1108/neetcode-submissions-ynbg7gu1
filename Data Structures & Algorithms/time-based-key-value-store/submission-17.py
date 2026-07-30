class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap[key]
        l = 0
        r = len(values) - 1
        ans = ""
        while l <= r:
            mid = (l+r) // 2
            if values[mid][1] <= timestamp:
                l = mid + 1
                ans = values[mid][0]
            else:
                r = mid - 1
        return ans

        

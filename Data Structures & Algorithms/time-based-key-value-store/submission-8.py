class TimeMap:

    def __init__(self):
        self.timestore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestore:
            self.timestore[key] = {}
        if timestamp not in self.timestore[key]:
            self.timestore[key][timestamp] = []
        self.timestore[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestore:
            return ""
        seen = 0
        for time in self.timestore[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.timestore[key][seen][-1]
                


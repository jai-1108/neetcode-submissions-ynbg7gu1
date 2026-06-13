class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = {}
        if timestamp not in self.timemap[key]:
            self.timemap[key][timestamp] = []
        self.timemap[key][timestamp].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        seen = 0
        for time in self.timemap[key]:
            if time <= timestamp:
                seen = max(seen, time) 
        return "" if seen == 0 else self.timemap[key][seen][0]       

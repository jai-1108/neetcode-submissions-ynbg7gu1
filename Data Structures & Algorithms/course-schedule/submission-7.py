class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [i for i in range(numCourses)]
        hashmap = defaultdict(list)
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            visited.add(crs)
            cycle.remove(crs)
            return True
        
        for crs in courses:
            if not dfs(crs):
                return False
        return True

        
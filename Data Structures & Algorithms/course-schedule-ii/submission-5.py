class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [c for c in range(numCourses)]
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        cycle = set()
        output = []
        visit = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for c in courses:
            if not dfs(c):
                return []
        return output

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [i for i in range(numCourses)]
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            visited.remove(crs)
            return True
        for course in courses:
            if not dfs(course):
                return False
        return True
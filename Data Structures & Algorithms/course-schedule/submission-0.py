class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = []
        for i in range(numCourses):
            courses.append(i)
        hashmap = defaultdict(list)
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if hashmap[crs] == []:
                return True
            visited.add(crs)
            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            hashmap[crs] = []
            return True
        for crs in courses:
            if not dfs(crs):
                return False
        return True

        
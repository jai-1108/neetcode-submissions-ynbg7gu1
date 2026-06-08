class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                array.append(matrix[i][j])
        l = 0
        r = len(array) - 1
        while l <= r:
            mid = (l + r)//2
            if array[mid] > target:
                r = mid - 1
            elif array[mid] < target:
                l = mid + 1
            else:
                return True
        return False
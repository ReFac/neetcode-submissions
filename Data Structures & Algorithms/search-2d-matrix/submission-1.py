class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        tSize = n*m
        left = 0
        right = tSize-1

        while left <= right:
            mid = left + (right - left)//2
            n1 = mid // m
            m1 = mid % m
            val = matrix[n1][m1]
            if val > target:
                right = mid -1
            elif val < target:
                left = mid + 1
            else:
                return True

        return False

        
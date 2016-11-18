# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        head = [x[0] for x in matrix]
        left, right = 0, len(head)-1
        while left < right:
            mid = (left + right) / 2
            if head[mid] == target:
                return True
            elif head[mid] < target:
                left = mid + 1
            elif head[mid] > target:
                right = mid - 1
        if head[left] > target:
            left -= 1
        head = matrix[left]
        left, right = 0, len(head)-1
        while left <= right:
            mid = (left + right) / 2
            if head[mid] == target:
                return True
            elif head[mid] < target:
                left = mid + 1
            elif head[mid] > target:
                right = mid - 1
        return False

if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    print Solution().searchMatrix(matrix, 3)
    print Solution().searchMatrix(matrix, 16)
    print Solution().searchMatrix(matrix, 50)
    print Solution().searchMatrix(matrix, 23)

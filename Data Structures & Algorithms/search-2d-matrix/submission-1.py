class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if matrix[middle][0] == target:
                return True

            elif matrix[middle][-1] < target:
                low = middle + 1

            elif matrix[middle][0] > target:
                high = middle - 1
                
            else:
                low = 0
                high = len(matrix[middle]) - 1

                while low <= high:
                    mid = low + (high - low) // 2

                    if matrix[middle][mid] == target:
                        return True

                    elif matrix[middle][mid] < target:
                        low = mid + 1

                    else:
                        high = mid -1 

                    
        return False
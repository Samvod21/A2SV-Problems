class Solution(object):
    def searchMatrix(self, matrix, target):
        r = len(matrix)
        c = len(matrix[0])
        ind = -1

        for i in range(r):
            if target <= matrix[i][c - 1]:
                ind = i
                break
        
        if ind == -1:
            return False
            exit()
        
        l = 0
        r = c - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[ind][mid] == target:
                return True
                exit()
            
            elif matrix[ind][mid] > target:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return False

        
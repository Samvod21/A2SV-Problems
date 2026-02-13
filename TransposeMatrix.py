class Solution(object):
    def transpose(self, matrix):
        ele = []
        res = []

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                ele.append(matrix[j][i])
            
            res.append(ele)
            ele = []
            
        return res
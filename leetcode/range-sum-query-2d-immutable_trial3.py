class NumMatrix(object):

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.prefixSum = [[]]
            return

        r, c = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(r):
            for j in range(c):
                self.prefixSum[i+1][j+1] = self.prefixSum[i][j+1] + self.prefixSum[i+1][j] - self.prefixSum[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        s = self.prefixSum[row2+1][col2+1] - self.prefixSum[row2+1][col1] - self.prefixSum[row1][col2+1] + self.prefixSum[row1][col1]
        return s
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
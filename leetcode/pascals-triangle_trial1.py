class Solution(object):
    def generate(self, numRows):
        ans = [[1]]

        for i in range(1, numRows):
            dirRow = [0] + ans[-1] + [0]
            normalRow = []

            for j in range(len(ans[-1]) + 1):
                normalRow.append(dirRow[j] + dirRow[j + 1])
            
            ans.append(normalRow)
        
        return ans
        
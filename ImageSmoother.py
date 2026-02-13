class Solution(object):
    def imageSmoother(self, img):
        row = len(img)
        col = len(img[0])
        result = []

        for _ in range(row):
            result.append([0] * col)

        for i in range(row):
            for j in range(col):
                total = 0
                count = 0

                for dr in [-1, 0, 1]: 
                    for dc in [-1, 0, 1]: 
                        nr = i + dr 
                        nc = j + dc

                        if 0 <= nr < row and 0 <= nc < col: 
                            total += img[nr][nc] 
                            count += 1 
                            result[i][j] = total // count
        
        return result
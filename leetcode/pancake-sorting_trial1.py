class Solution(object):
    def pancakeSort(self, arr):
        res = []

        for i in range(len(arr), 1, -1):
            x = arr.index(i)

            if x == i - 1:
                continue
            
            if x != 0:
                res.append(x + 1)
                arr[:x + 1] = arr[:x + 1][::-1]
            
            res.append(i)
            arr[:i] = arr[:i][::-1]
        
        return res
            



        
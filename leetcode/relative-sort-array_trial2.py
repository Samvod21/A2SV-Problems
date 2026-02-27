class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        sort1 = []
        nots = []

        for i in arr2:
            for j in arr1:
                if i == j:
                    sort1.append(j)
        
        for i in arr1:
            if i not in arr2:
                nots.append(i)
        
        nots.sort()

        for i in nots:
            sort1.append(i)
        
        return sort1
        
class Solution(object):
    def findRestaurant(self, list1, list2):
        indexes = []
        sums = []
        result = []

        for i in range(0, len(list1)):
            for j in range(0, len(list2)):
                if list1[i] == list2[j]:
                    indexes.append([i,j])
        
        for i,j in indexes:
            sums.append(i + j)
        
        sums.sort()

        for i,j in indexes:
            if i + j == sums[0]:
                result.append(list1[i])
        
        return result
#2 10
from collections import defaultdict

class Solution(object):
    def numberOfBoomerangs(self, points):
        res = 0

        for i in points:
            distance = defaultdict(int)

            for j in points:
                if i == j:
                    continue
                
                x = i[0] - j[0]
                y = i[1] - j[1]
                dis = x**2 + y**2
                distance[dis] += 1
            
            for counts in distance.values():
                res += counts * (counts - 1)
        
        return res
# 2 25
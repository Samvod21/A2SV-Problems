from collections import Counter
class Solution(object):
    def findWinners(self, matches):
        loss = Counter()
        players = set()
        zeros = []
        ones = []

        for i, j in matches:
            players.add(i)
            players.add(j)
            loss[j] += 1
        
        for p in players:
            if loss[p] == 0:
                zeros.append(p)
            elif loss[p] == 1:
                ones.append(p)
        
        zeros.sort()
        ones.sort()

        return [zeros, ones]
# 3 28
class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        psize = len(players)
        tsize = len(trainers)
        players.sort()
        trainers.sort()
        p = 0
        t = 0
        c = 0

        while p < psize and t < tsize:
            if players[p] <= trainers[t]:
                c += 1
                p += 1
                t += 1
            
            else:
                t += 1
        
        return c

        
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        turn = abs(target[0]) + abs(target[1])
        
        for i, j in ghosts:
            dist = abs(i - target[0]) + abs(j - target[1])

            if dist <= turn:
                return False
        
        return True
#4 39
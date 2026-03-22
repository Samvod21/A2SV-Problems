class Solution(object):
    def minimumRecolors(self, blocks, k):
        l = 0
        whites = 0
        recolored = float("inf")

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                whites += 1
            
            if r - l + 1 == k:
                recolored = min(recolored, whites)

                if blocks[l] == 'W':
                    whites -= 1
                
                l += 1
        
        return recolored
        
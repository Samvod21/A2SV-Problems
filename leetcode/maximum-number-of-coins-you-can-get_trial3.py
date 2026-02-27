class Solution(object):
    def maxCoins(self, piles):
        triplet = []
        count = 0
        rounds = len(piles) / 3
        piles.sort()

        for i in range(1, rounds + 1):
            ind = len(piles) - 2 * i
            count += piles[ind]

        
        return count





        
        
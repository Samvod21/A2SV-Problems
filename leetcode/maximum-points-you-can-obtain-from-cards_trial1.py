class Solution(object):
    def maxScore(self, cardPoints, k):
        total = sum(cardPoints)
        winsize = len(cardPoints) - k

        if winsize == 0:
            return total
        
        s = sum(cardPoints[:winsize])
        minsum = s

        for i in range(winsize, len(cardPoints)):
            s += cardPoints[i]
            s -= cardPoints[i - winsize]

            minsum = min(minsum, s)
        
        return total - minsum

        
        
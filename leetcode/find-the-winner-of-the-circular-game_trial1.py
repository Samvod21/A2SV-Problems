class Solution(object):
    def findTheWinner(self, n, k):
        circular = []
        start = 0

        for i in range(1, n + 1):
            circular.append(i)

        while len(circular) != 1:
            nextval = (start + k - 1) % len(circular)
            circular.pop(nextval)
            start = nextval
        
        return circular[0]


        
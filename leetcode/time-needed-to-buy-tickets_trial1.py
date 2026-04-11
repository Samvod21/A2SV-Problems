class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        c = 0
        target = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                c += min(target, tickets[i])
            
            else:
                c += min(target - 1, tickets[i])
        
        return c

            
        
        return c - non


        
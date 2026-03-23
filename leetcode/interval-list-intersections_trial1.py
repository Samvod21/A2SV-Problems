class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        res = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            fstart, fend = firstList[i]
            sstart, send = secondList[j]

            if fstart <= send and sstart <= fend:
                x = max(fstart, sstart) 
                y = min(fend, send)
                res.append([x, y])
            
            if fend < send:
                i += 1
            else:
                j += 1
        
        return res

        
        
class Solution(object):
    def merge(self, intervals):
        size = len(intervals)
        merged = []
        intervals.sort()
        first = intervals[0]

        if size == 1:
            merged.append(first)
            return merged
        
        for i in range(1, size):
            next = intervals[i]

            if first[1] >= next[0]:
                first[1] = max(first[1], next[1])
                #merged.append(first)
            
            else:
                merged.append(first)
                first = next
        
        merged.append(first)
        return merged

        
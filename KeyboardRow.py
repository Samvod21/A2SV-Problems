class Solution(object):
    def findWords(self, words):
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        #isFirst = True
        #isSecond = True
        #isThird = True
        result = []

        for i in words:
            lower = set(i.lower()) 
            
            if lower.issubset(first) or lower.issubset(second) or lower.issubset(third): 
                result.append(i)
        
        return result

# 4 46
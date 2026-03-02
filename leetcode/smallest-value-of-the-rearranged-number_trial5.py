class Solution(object):
    def smallestNumber(self, num):
        dig = []
        res = 0
        
        if num in range(-9, 10):
            return num
        
        elif num < 0:
            num1 = abs(num)
            
            while num1 != 0:
                rem = num1 % 10
                dig.append(rem)
                num1 //= 10
            
            dig.sort()
            dig.reverse()
            
            for i in dig:
                res = res * 10 + i
       
            return -1 * res
        
        else:
            while num != 0:
                rem = num % 10
                dig.append(rem)
                num //= 10
        
        
            dig.sort()
        
            if dig[0] == 0:
                for i in range(1, len(dig)):
                    if dig[i] != 0:
                        dig[0], dig[i] = dig[i], dig[0]
                        break
                
            for i in dig:
                res = res * 10 + i
       
            return res

        
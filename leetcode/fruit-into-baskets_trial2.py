class Solution(object):
    def totalFruit(self, fruits):
        l = 0
        fruitfre = {}
        maximum = 0

        for r in range(len(fruits)):
            fruitfre[fruits[r]] = fruitfre.get(fruits[r], 0) + 1

            while len(fruitfre) > 2:
                fruitfre[fruits[l]] -= 1

                if fruitfre[fruits[l]] == 0:
                    del fruitfre[fruits[l]]
                
                l += 1
            
            maximum = max(maximum, r - l + 1)
        
        return maximum




        
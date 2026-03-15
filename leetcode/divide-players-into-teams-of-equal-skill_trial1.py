class Solution(object):
    def dividePlayers(self, skill):
        total = 0
        skill.sort()
        n = len(skill)
        target = skill[0] + skill[-1]
        #teams = []
        size = n // 2
        
        for i in range(size):
            if skill[i] + skill[n - 1 - i] != target:
                return -1
            
            total += skill[i] * skill[n - 1 - i]
        
        return total

                
        
        
            
        


        
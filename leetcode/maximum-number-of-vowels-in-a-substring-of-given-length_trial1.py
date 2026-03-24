class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        maximum = 0
        c = 0
        
        for i in range(k):
            if s[i] in vowels:
                c += 1
        maximum = c
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                c += 1
            
            if s[i - k] in vowels:
                c -= 1
            
            maximum = max(maximum, c)
            
        
        return maximum


            
        

        
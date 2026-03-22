class Solution(object):
    def countVowelSubstrings(self, word):
        c = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        start = 0
        lastvowel = {}

        for i, j in enumerate(word):
            if j in vowels:
                lastvowel[j] = i
                
                if len(lastvowel) == 5:
                    first = min(lastvowel.values())
                    c += first - start + 1
            
            else:
                lastvowel = {}
                start = i + 1
        
        return c

        
        return c
        
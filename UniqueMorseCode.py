class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_code = set()
        trans = ""
        letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
        Code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        Morse = dict(zip(letters, Code))
        
        for i in words:
            for j in i:
                trans += Morse[j]
            
            morse_code.add(trans)
            trans = ""
        
        return len(morse_code)
# 4 31
class Solution(object):
    def shiftingLetters(self, s, shifts):
        chars = list(s)
        sh = [0] * (len(chars) + 1)

        for i, j, k in shifts:
            val = 1 if k == 1 else -1
            sh[i] += val
    
            if j + 1 <= len(chars):
                sh[j + 1] -= val
    
        current = 0

        for i in range(len(chars)):
            current += sh[i]
            shift = current % 26
            new_char = (ord(chars[i]) - ord('a') + shift) % 26
            chars[i] = chr(ord('a') + new_char)
    
        return "".join(chars)
        
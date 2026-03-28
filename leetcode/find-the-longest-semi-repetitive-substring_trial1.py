class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        chars = [0]
        maximum = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                chars.append(i)
        
        chars.append(len(s))

        for i in range(1, len(chars) - 1):
            val = chars[i + 1] - chars[i - 1]
            maximum = max(maximum, val)
        
        if len(chars) == 2:
            return len(s)
        
        return maximum
        
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        win = {}
        maxlen = 0

        for r in range(len(s)):
            win[s[r]] =win.get(s[r], 0) + 1

            while l < len(s) and len(win) != (r - l + 1):
                win[s[l]] -= 1

                if win[s[l]] == 0:
                    del win[s[l]]
                
                l += 1
            
            maxlen = max(maxlen, r - l + 1)
        
        return maxlen

        
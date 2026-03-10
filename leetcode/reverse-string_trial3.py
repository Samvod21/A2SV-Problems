class Solution(object):
    def reverseString(self, s):
        size = len(s)
        f = 0
        l = size - 1

        while f < l:
            s[f], s[l] = s[l], s[f]
            f += 1
            l -= 1
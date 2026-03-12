class Solution(object):
    def minWindow(self, s, t):
        tfre = Counter(t)
        window = Counter()
        l = 0
        r = 0
        valid = 0
        st = 0
        size = float("inf")

        while r < len(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in tfre and window[c] == tfre[c]:
                valid += 1

            while valid == len(tfre):
                if r - l + 1 < size:
                    st = l
                    size = r - l + 1

                dis = s[l]
                window[dis] -= 1

                if dis in tfre and window[dis] < tfre[dis]:
                    valid -= 1
                
                l += 1
            
            r += 1
        
        if size != float("inf"):
            return s[st:st + size]
        
        else:
            return ""

        
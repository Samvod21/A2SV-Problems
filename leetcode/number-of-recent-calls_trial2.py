class RecentCounter(object):

    def __init__(self):
        self.requests = []
        self.begin = 0

    def ping(self, t):
        self.requests.append(t)

        while self.requests[self.begin] < t - 3000:
            self.begin += 1
    
        res = len(self.requests) - self.begin

        return res
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
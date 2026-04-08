class DataStream(object):

    def __init__(self, value, k):
        self.val = value
        self.size = k
        self.c = 0
        

    def consec(self, num):
        if num == self.val:
            self.c += 1
        
        else:
            self.c = 0
        
        if self.c >= self.size:
            return True
        
        return False
        

        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
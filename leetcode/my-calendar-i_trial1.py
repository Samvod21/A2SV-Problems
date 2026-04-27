class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def book(self, startTime, endTime):
        for s, e in self.calendar:
            if startTime < e and endTime > s:
                return False
            
        self.calendar.append((startTime, endTime))
        return True
            


        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        ans = [0] * (n + 1)

        for i in bookings:
            ans[i[0] - 1] += i[2]
            ans[i[1]] -= i[2]
        
        current = 0

        for i in range(n):
            current += ans[i]
            ans[i] = current
        
        for i in range(len(ans)):
            if i >= n:
                ans.pop(i)
        
        return ans
        
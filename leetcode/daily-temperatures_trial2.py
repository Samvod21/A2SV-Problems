class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ind = stack.pop()
                ans[ind] = i - ind
            
            stack.append(i)
            

        return ans

        
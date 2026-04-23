class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] < -1 * i:
                    stack.pop()
                    continue
                
                elif stack[-1] == -1 * i:
                    stack.pop()
                    break
                
                else:
                    break
            
            else:
                stack.append(i)
        
        return stack

        
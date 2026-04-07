class Solution(object):
    def isValid(self, s):
        if len(s) == 1:
            return False
        
        if s == "":
            return True
        
        stack = []
        opening = {'{', '[', '('}

        for char in s:
            if char in opening:
                stack.append(char)
            
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()

                if top == '{' and char != '}':
                    return False
                
                if top == '[' and char != ']':
                    return False
                
                if top == '(' and char != ')':
                    return False
        
        if len(stack) == 0:
            return True
        
        else:
            return False
            
        
        
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = {"+", "-", "*", "/"}

        for i in tokens:
            if i not in operators:
                stack.append(int(i))

            else:
                a = stack.pop()
                b = stack.pop()
                
                if i == "+":
                    stack.append(b + a)

                elif i == "-":
                    stack.append(b - a)

                elif i == "*":
                    stack.append(b * a)
                    
                elif i == "/":
                    stack.append(int(float(b) / a))
        
        return stack[0]
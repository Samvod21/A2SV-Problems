class Solution(object):
    def decodeString(self, s):
        l = 0
        num = 0
        stack = [""]

        while l < len(s):
            if s[l].isdigit():
                num = num * 10 + int(s[l])
            
            elif s[l] == "[":
                stack.append(num)
                num = 0
                stack.append("")
            
            elif s[l] == "]":
                n1 = stack.pop()
                times = stack.pop()
                n2 = stack.pop()
                stack.append(n2 + n1 * times)
            
            else:
                stack[-1] += s[l]
            
            l += 1
        
        return "".join(stack)
        
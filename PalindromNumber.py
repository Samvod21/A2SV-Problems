def isPalindrome(x):
    s = str(x)

    if s == s[::-1]:
        return True
        
    return False

print(isPalindrome(-121))
#21

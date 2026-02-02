def isCovered(ranges, left, right):
    for nums in range(left, right + 1):
        if not any(r[0] <= nums <= r[1] for r in ranges):
            return False
        
    return True
#35        
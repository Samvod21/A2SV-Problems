class Solution(object):
    def carFleet(self, target, position, speed):
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        res = 0
        cur = 0

        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t

        return res
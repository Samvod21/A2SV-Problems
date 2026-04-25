class Solution(object):
    def nextGreatestLetter(self, letters, target):
        l, r = 0, len(letters) - 1

        if target >= letters[r]:
            return letters[0]

        while l <= r:
            mid = l + (r - l) // 2

            if letters[mid] > target:
                r = mid - 1
            
            else:
                l = mid + 1
        

        return letters[l]
        
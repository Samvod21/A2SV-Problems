class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for n1 in nums1:
            vals = -1
            found = False

            for n2 in nums2:
                if n2 == n1:
                    found = True
                
                if found == True:
                    if n2 > n1:
                        vals = n2
                        break

            ans.append(vals)
        
        return ans
        
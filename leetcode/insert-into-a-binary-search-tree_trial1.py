# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        node = root

        while True:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                
                node = node.left
            
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                
                node = node.right

        return root
        
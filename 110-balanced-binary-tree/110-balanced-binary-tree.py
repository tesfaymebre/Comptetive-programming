# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        truth = set()
        
        def recur(node):
            
            if not node:
                return 0
            
            d1 = 1 + recur(node.left)
            d2 = 1 + recur(node.right)
            
            if abs(d1 - d2) > 1:
                truth.add(0)
                
            return max(d1,d2)
        
        recur(root)
        
        if 0 in truth:
            return False
        
        return True
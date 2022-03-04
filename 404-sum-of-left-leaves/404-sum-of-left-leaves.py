# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.total = 0
        
        def recur(node, l_r):
            if not node:
                return
            
            if not node.left and not node.right:
                if l_r == 0:
                    self.total += node.val
                return
            
            if node.left:
                recur(node.left,0)
                
            if node.right:
                recur(node.right,1)
                
        recur(root.left,0)
        recur(root.right,1)
        
        return self.total
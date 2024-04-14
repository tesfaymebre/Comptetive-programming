# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.total = 0
        
        def recur(node, left):
            if not node:
                return
            
            if not node.left and not node.right:
                if left:
                    self.total += node.val
                return
            
            recur(node.left,1)
            recur(node.right,0)
                
        recur(root,0)
        
        return self.total
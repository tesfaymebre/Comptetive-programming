# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur(node, lower, upper):
            
            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            if not recur(node.right, node.val, upper):
                return False
            
            if not recur(node.left, lower, node.val):
                return False
            
            return True
        
        return recur(root, float('-inf'), float('inf'))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.result = max(self.result,left*(total-left),right*(total-right))
            return left + right + node.val
        
        
        self.result = 0
        total = 0
        
        total = dfs(root)
        dfs(root)
        
        return self.result % (10**9 + 7)
        
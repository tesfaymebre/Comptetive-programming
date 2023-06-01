# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dp(node):
            if node not in memo:
                if not node:
                    return 0
                
                pick = node.val
                if node.left:
                    pick += dp(node.left.left) + dp(node.left.right)
                    
                if node.right:
                    pick += dp(node.right.left) + dp(node.right.right)
                    
                not_pick = dp(node.left) + dp(node.right)
                
                memo[node] = max(pick,not_pick)
                
            return memo[node]
                
        memo = {}
        return dp(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            path_sum = left + right + node.val
            self.max_path_sum = max(self.max_path_sum,path_sum)
            
            return max(left,right) + node.val
            
        self.max_path_sum = float('-inf')
        dfs(root)
        
        return self.max_path_sum
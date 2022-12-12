# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node,seen):
            if node.val in seen:
                seen.remove(node.val)
            else:
                seen.add(node.val)
                
            if not node.left and not node.right:
                return 1 if len(seen) <= 1 else 0
            
            left = 0
            
            if node.left:
                left = dfs(node.left,seen.copy())
              
            right = 0
            
            if node.right:
                right = dfs(node.right,seen.copy())
                
            return left + right
        
        return dfs(root,set())
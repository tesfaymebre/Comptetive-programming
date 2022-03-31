# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        self.max_depth = 1
        
        def dfs(node,curr_depth):
            if not node:
                return
            
            if self.max_depth < curr_depth:
                self.max_depth = curr_depth
                self.ans = node.val
            
            dfs(node.left,curr_depth+1)
            dfs(node.right,curr_depth+1)
                
        dfs(root,1)
        return self.ans
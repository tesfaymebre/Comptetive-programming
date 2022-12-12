# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            left = False
            
            if node.left:
                left = dfs(node.left)
                
            right = False
            
            if node.right:
                right = dfs(node.right)
                
            if left:
                node.left = None
            if right:
                node.right = None
                
            if not node.left and not node.right:
                return node.val == target
            
            return False
        
        dummy = dfs(root)
        
        if dummy:
            return None
        
        return root
            
            
                
            
                
        
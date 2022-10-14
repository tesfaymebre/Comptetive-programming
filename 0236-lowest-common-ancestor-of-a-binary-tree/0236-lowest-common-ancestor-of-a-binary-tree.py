# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,val):
            if not node:
                return False
            if node.val == val:
                return True
            
            return dfs(node.left,val) or dfs(node.right,val)
        
        def dfs_top(node,p_val,q_val):
            nonlocal ans
            
            if not node:
                return False
            if node.val == p_val or node.val == q_val:
                return True
            
            left = dfs_top(node.left,p_val,q_val) 
            right = dfs_top(node.right,p_val,q_val)
            
            if left and right:
                ans = node
                return
            return left or right
            
                
        
        if dfs(p,q.val):
            return p
        elif dfs(q,p.val):
            return q
        else:
            ans = None
            dfs_top(root,p.val,q.val)
            return ans
        
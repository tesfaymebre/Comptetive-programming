# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count_good_nodes = 0
        
        def dfs(node,prev_max):
            nonlocal count_good_nodes
            
            if not node:
                return
            
            if node.val >= prev_max:
                count_good_nodes += 1
                
            prev_max = max(prev_max,node.val)
            
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)
            
            return
        
        dfs(root,float('-inf'))
        
        return count_good_nodes
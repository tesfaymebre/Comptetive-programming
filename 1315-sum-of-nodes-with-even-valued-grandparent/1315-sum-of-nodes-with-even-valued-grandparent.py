# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        
        def dfs(node, grandpa):
            if not node.left and not node.right:
                return
            
            even = True if grandpa % 2 == 0 else False
            
            if node.left:
                
                if node.left.left and even:
                    self.total += node.left.left.val
                if node.left.right and even:
                    self.total += node.left.right.val
                    
                dfs(node.left, node.left.val)
                
            if node.right:
                if node.right.left and even:
                    self.total += node.right.left.val
                if node.right.right and even:
                    self.total += node.right.right.val
                    
                dfs(node.right, node.right.val)
                
        dfs(root, root.val)
        return self.total
            
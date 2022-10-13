# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def BST(node, lower, upper):
            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            return BST(node.right, node.val, upper) and BST(node.left, lower, node.val)
        
        return BST(root, float('-inf'), float('inf'))
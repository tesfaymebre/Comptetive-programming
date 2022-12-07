# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        
        def in_order(node):
            if not node:
                return 0
            
            curr_sum = in_order(node.left) + in_order(node.right)
            
            if low <= node.val <= high:
                curr_sum += node.val
                 
            return curr_sum
        
        return in_order(root)
                
            
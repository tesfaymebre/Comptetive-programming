# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def recur(root,targetSum,curr_sum = 0):
            if not root:
                return False
            
            curr_sum += root.val
            
            if not root.left and not root.right and curr_sum == targetSum:
                return True
            
            return recur(root.left,targetSum, curr_sum) or recur(root.right,targetSum, curr_sum)
        
        return recur(root,targetSum)
        
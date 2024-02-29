# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        max_BST_sum = 0
        
        def isBST(node):
            nonlocal max_BST_sum
            
            if not node:
                return (0,True,float('inf'),float('-inf'))
            
            left,l_is_BST,l_min,l_max = isBST(node.left)
            right,r_is_BST,r_min,r_max = isBST(node.right)
            
            if l_is_BST and r_is_BST and node.val > l_max and node.val < r_min:
                curr_sum = left + node.val + right
                max_BST_sum = max(max_BST_sum,curr_sum)

                l_max = max(l_max,r_max,node.val)
                r_min = min(l_min,r_min,node.val)

                return (curr_sum , True,r_min,l_max)
            
            return (max(left,right), False,r_min,l_max)
        
        isBST(root)
        
        return max_BST_sum 
                    
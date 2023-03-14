# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def calcAverage(root):
            nonlocal count
            
            if not root:
                return [0, 0]
            
            left = calcAverage(root.left)
            right = calcAverage(root.right)
            
            sums = right[0] + left[0] + root.val
            n = right[1] + left[1] + 1
            
            if sums//n == root.val:
                count += 1 
                
            return [sums, n]
        
        count = 0
        calcAverage(root)
        return count
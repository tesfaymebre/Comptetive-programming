# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # solution 1 using recursion
        
        self.ans = []
        
        def recur(node):
            
            if not node:
                return None
            
            recur(node.left)
            recur(node.right)
            self.ans.append(node.val)
            
        recur(root)
        
        return self.ans
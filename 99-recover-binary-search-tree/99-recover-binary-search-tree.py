# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            inorder.append(node)
            dfs(node.right)
            
        inorder = []
        dfs(root)
        
        p1 = 0
        p2 = len(inorder) - 1
        
        while p1 < len(inorder):
            if inorder[p1].val > inorder[p1 + 1].val:
                break
            p1 += 1
        while p2 > 0:
            if inorder[p2].val < inorder[p2 - 1].val:
                break
            p2 -= 1
        inorder[p1].val,inorder[p2].val = inorder[p2].val, inorder[p1].val
            
        
        
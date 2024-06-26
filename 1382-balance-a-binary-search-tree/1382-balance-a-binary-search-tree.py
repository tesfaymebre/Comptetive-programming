# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        def balance(left,right):
            if left > right:
                return None
            
            if left == right:
                return TreeNode(inorder[left])
            
            mid = left + (right - left) // 2
            node = TreeNode(inorder[mid])
            node.left = balance(left,mid-1)
            node.right = balance(mid+1,right)
            
            return node
        
        return balance(0,len(inorder)-1)
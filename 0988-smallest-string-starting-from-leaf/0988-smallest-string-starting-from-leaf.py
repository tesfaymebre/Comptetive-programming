# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return []
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            left.append(node.val)
            right.append(node.val)
            
            if len(left) == 1:
                return right
            
            if len(right) == 1:
                return left
            
            for a,b in zip(left,right):
                if a < b:
                    return left
                elif b < a:
                    return right
            
            if len(left) <= len(right):
                if root == node:
                    return left
                
                return right
            
            if root == node:
                return right
            
            return left
        
        res = dfs(root)
        
        ascii = ord('a')
        res = [chr(ascii + i) for i in res]
        
        return "".join(res)
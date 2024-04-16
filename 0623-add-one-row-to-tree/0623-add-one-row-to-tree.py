# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        
        def dfs(node,level):
            if depth - 1 == level:
                left_new_node = TreeNode(val)
                right_new_node = TreeNode(val)
                
                left_new_node.left = node.left
                right_new_node.right = node.right
                
                node.left = left_new_node
                node.right = right_new_node
                
                return 
            
            if node.left:
                dfs(node.left, level + 1)
                
            if node.right:
                dfs(node.right, level + 1)
                
        dfs(root, 1)
        
        return root
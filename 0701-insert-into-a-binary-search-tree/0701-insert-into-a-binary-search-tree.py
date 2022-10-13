# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        
        def DFS(node,new_node):
            if node.val > new_node.val and not node.left:
                node.left = new_node
                return
            elif node.val > new_node.val:
                DFS(node.left,new_node)
            elif not node.right:
                node.right = new_node
                return
            else:
                DFS(node.right,new_node)
             
        if root:
            DFS(root,new_node)
        else:
            root = new_node
            
        return root
                    
                    
                    
                
            
        
        
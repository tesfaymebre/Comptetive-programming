# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successor(node):
            mini = node.val
            while node.left:
                node = node.left
                mini = node.val
                
            return mini
        
        def BST_del(node,key):
            if not node: 
                return None
            if node.val > key:
                node.left = BST_del(node.left, key)
            elif node.val < key:
                node.right= BST_del(node.right, key)
            else: 
                if not node.right: 
                    return node.left
                if not node.left: 
                    return node.right
                    
                node.val = successor(node.right)
                node.right = BST_del(node.right,node.val)
            return node
        
        return BST_del(root,key)
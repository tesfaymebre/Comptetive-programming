# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(postorder[-1])
        val_indx = dict()
        
        for i,val in enumerate(inorder):
            val_indx[val] = i
        
        for i in range(len(postorder)-2,-1,-1):
            curr = root
            new_node = TreeNode(postorder[i])
            while True:
                if val_indx[postorder[i]] < val_indx[curr.val]:
                    if not curr.left:
                        curr.left = new_node
                        break
                    curr = curr.left     
                else:
                    if not curr.right:
                        curr.right = new_node
                        break
                    curr = curr.right
                        
        return root
            
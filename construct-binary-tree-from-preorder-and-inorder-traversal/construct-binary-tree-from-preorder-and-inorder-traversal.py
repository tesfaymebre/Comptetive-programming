# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:  
        preorder = deque(preorder)
        val_indx = {val: i for i, val in enumerate(inorder)}
        
        def recur(start, end):
            if start > end:
                return None
            
            node = TreeNode(preorder.popleft())
            mid = val_indx[node.val]
            
            node.left = recur(start, mid - 1)
            node.right = recur(mid + 1, end)
            return node
        
        return recur(0, len(inorder) - 1)
            
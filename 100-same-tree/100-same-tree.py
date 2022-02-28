# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def recur(p,q):
            if (p and q)  and p.val != q.val:
                return False

            if not p and not q:
                return True

            if (p and not q) or (q and not p):
                print('c')
                return False

            return recur(p.left, q.left) and recur(p.right, q.right)
        
        return recur(p,q)
    
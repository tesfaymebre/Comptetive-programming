# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def dfs(node,p_val,q_val):
            if not node:
                return None

            if node.val == p_val or node.val == q_val:
                return node

            left = dfs(node.left,p_val,q_val)
            right = dfs(node.right,p_val,q_val)

            if left and right:
                return node

            return left or right

        return dfs(root,p.val,q.val)
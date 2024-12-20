# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(l_child,r_child,level):
            if not l_child or not r_child:
                return

            if level & 1 == 0:
                l_child.val,r_child.val = r_child.val, l_child.val

            dfs(l_child.left,r_child.right, level+1)
            dfs(l_child.right,r_child.left, level+1)

        dfs(root.left,root.right,0)

        return root
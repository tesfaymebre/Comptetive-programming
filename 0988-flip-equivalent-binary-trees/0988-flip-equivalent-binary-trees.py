# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if node2.left and node2.right:
                if not node1.left or not node1.right:
                    return False

            if node1.left:
                if node2.left and node1.left.val == node2.left.val:
                    if not dfs(node1.left,node2.left):
                        return False
                elif node2.right and node1.left.val == node2.right.val:
                    if not dfs(node1.left,node2.right):
                        return False
                else:
                    return False

            if node1.right:
                if node2.left and node1.right.val == node2.left.val:
                    if not dfs(node1.right,node2.left):
                        return False
                elif node2.right and node1.right.val == node2.right.val:
                    if not dfs(node1.right,node2.right):
                        return False
                else:
                    return False

            return True

        if (root1 and not root2) or (not root1 and root2):
            return False

        if not root1 and not root2:
            return True

        if root1.val != root2.val:
            return False

        return dfs(root1,root2)
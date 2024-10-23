# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev_level_sum = root.val
        queue = deque([root])

        while queue:
            new_level_sum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                node.val = prev_level_sum - node.val

                if node.left:
                    new_level_sum += node.left.val
                    queue.append(node.left)

                if node.right:
                    new_level_sum += node.right.val
                    queue.append(node.right)

                if node.left and node.right:
                    node.left.val += node.right.val
                    node.right.val = node.left.val

            prev_level_sum = new_level_sum

        return root
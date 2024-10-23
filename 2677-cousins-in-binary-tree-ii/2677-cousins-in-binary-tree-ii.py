# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = defaultdict(int)
        level = 0
        queue = deque([root])

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                total[level] += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

        root.val = 0
        queue.append(root)
        level = 1

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                temp = 0
                if node.left:
                    queue.append(node.left)
                    temp += node.left.val

                if node.right:
                    queue.append(node.right)
                    temp += node.right.val

                if node.left:
                    node.left.val = total[level] - temp

                if node.right:
                    node.right.val = total[level] - temp

            level += 1

        return root
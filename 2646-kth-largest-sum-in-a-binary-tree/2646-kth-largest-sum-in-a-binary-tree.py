# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []

        queue = deque([root])

        while queue:
            size = len(queue)
            curr_total = 0

            for i in range(size):
                node = queue.popleft()
                curr_total += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            sums.append(curr_total)

        if len(sums) < k:
            return -1
            
        sums.sort()

        return sums[-k]
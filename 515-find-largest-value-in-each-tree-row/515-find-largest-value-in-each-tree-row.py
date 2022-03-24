# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque()
        queue.append(root)
        
        while queue:
            n = len(queue)
            max_val = queue[0].val
            for i in range(n):
                temp = queue.popleft()
                max_val = max(max_val, temp.val)
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            ans.append(max_val)
        
        return ans
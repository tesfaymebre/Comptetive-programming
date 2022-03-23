# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        ans = []
        
        queue.append(root)
        
        while queue:
            n = len(queue)
            inner_list = []
            
            for i in range(n):
                temp = queue.popleft()
                inner_list.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                    
            ans.append(inner_list)
                    
        return ans
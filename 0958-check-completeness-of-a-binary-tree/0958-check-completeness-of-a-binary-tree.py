# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        flag = False
        queue = deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                
                if not node:
                    flag = True
                    continue
                    
                if flag:
                    return False
                
                queue.append(node.left)
                queue.append(node.right)
                
        return True
                
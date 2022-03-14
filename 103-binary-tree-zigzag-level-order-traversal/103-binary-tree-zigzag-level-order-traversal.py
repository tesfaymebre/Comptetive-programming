# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        ans = []
        level = 0
        queue.append(root)
        
        while queue:
            n = 0
            ans_list = []
            n = len(queue)
            
            for i in range(n):
                if level %2 == 0:
                    curr = queue.popleft()
                    ans_list.append(curr.val)
                    if curr.left:
                        queue.append(curr.left) 
                    if curr.right:
                        queue.append(curr.right) 
                else:
                    curr = queue.pop()
                    ans_list.append(curr.val)
                    if curr.right:
                        queue.appendleft(curr.right)
                    if curr.left:
                        queue.appendleft(curr.left)            
            ans.append(ans_list) 
            level += 1 
                
        return ans
               
                
        
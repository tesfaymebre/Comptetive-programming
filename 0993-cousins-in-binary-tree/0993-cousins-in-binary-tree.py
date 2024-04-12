# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque()
        queue.append((root,0))
        
        depth_parent = []
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                node,depth = queue.popleft()
                
                if node.left:
                    if node.left.val in [x,y]:
                        depth_parent.append((depth+1,node.val))
                    
                    queue.append((node.left,depth + 1))
                
                if node.right:
                    if node.right.val in [x,y]:
                        depth_parent.append((depth + 1, node.val))
                    
                    queue.append((node.right,depth + 1))
        
        if len(depth_parent) < 2:
            return False
        
        if depth_parent[0][0] == depth_parent[1][0] and depth_parent[0][1] != depth_parent[1][1]:
            return True
        
        return False
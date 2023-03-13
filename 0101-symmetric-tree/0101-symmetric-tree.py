# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #solution 1 using BFS
        
        queue = deque([root])
        while queue:
            n = len(queue)
            
            p1 = 0
            p2 = n - 1 
            while p1 < p2:
                if not queue[p1] and not queue[p2]:
                    p1 += 1
                    p2 -= 1 
                    continue
                elif not queue[p1] and queue[p2] or (not queue[p2] and queue[p1]) or \
                        (queue[p1].val != queue[p2].val):
                    return False
                
                p1 += 1
                p2 -= 1
                
            for node in range(n):
                curr = queue.popleft()
                if curr:
                    if curr and curr.left:
                        queue.append(curr.left)
                    else:
                        queue.append(None)

                    if curr and curr.right:
                        queue.append(curr.right)
                    else:
                        queue.append(None)
        return True
        
        #solution 2 using DFS
#         def recur(node1, node2):
#             if not node1 and not node2:
#                 return True
            
#             if (node1 and not node2) or (not node1 and node2) or node1.val != node2.val:
#                 return False
            
#             return recur(node1.left, node2.right) and recur(node1.right, node2.left)
        
#         return recur(root.left, root.right)
        

        
        
            
            
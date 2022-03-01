# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #solution 1 using recursive
        
        self.total = 0
        
        def recur(node,value):
            if not node.left and not node.right:
                self.total += int(value)
                return 
            
            if node.left:
                recur(node.left, 10 * value + node.left.val)
                
            if node.right:
                recur(node.right, 10 * value + node.right.val)
        
        recur(root,root.val)
        
        return self.total   
            
        
        #solution 2 using iteratively
        
#         if not root.left and not root.right:
#             return root.val
        
#         stack = []
#         total = 0
#         visited = set()
        
#         stack.append(root)
        
#         while stack:
            
#             if stack[-1].left and stack[-1].left not in visited:
#                 stack.append(stack[-1].left)
#             elif stack[-1].right and stack[-1].right not in visited:
#                 stack.append(stack[-1].right)
#             elif stack[-1].left in visited or stack[-1].right in visited:
#                 visited.add(stack.pop())
#             else:
#                 st = 0
#                 j = 0
#                 for i in range(len(stack)-1,-1,-1):
#                     st+= stack[j].val * (10 ** i)
#                     j += 1
#                 total += st
#                 visited.add(stack.pop())
        
#         return total
                
            
            
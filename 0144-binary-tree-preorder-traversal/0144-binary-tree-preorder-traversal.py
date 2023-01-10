# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         solution 1 using recursive
#         self.ans = []
        
#         def recur(node):
            
#             if not node:
#                 return None
            
#             self.ans.append(node.val)
#             recur(node.left)
#             recur(node.right)
        
#         recur(root)
        
#         return self.ans
        
        
        
        #solution 2 using iteratively
        if not root:
            return []
        
        stack = []
        visited = set()
        ans = []
        
        stack.append(root)
        visited.add(root)
        ans.append(root.val)
        
        while stack:
            
            if stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
                visited.add(stack[-1])
                ans.append(stack[-1].val)
            elif stack[-1].right and stack[-1].right not in visited:
                stack.append(stack[-1].right)
                visited.add(stack[-1])
                ans.append(stack[-1].val)  
            else:
                stack.pop()
        
        return ans
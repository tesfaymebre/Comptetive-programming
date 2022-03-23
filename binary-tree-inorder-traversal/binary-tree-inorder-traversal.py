# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #solution 1 using recursive
        
#         self.ans = []
        
#         def recur(node):
#             if not node:
#                 return None
            
#             recur(node.left)
#             self.ans.append(node.val)
#             recur(node.right)
        
#         recur(root)
#         return self.ans
    
        
        #solution 2 using iteratively
        
        if not root:
            return []
        
        visited = set()
        stack = []
        ans = []
        
        stack.append(root)
        visited.add(root)
        
        while stack:
            if stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
                visited.add(stack[-1])
                
            else:
                temp = stack.pop()
                ans.append(temp.val)
                visited.add(temp)
                
                if temp.right:
                    stack.append(temp.right)
            
        return ans
                    
                
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        stack = []
        visited = set()
        ans = []
        
        stack.append(root)
        visited.add(root)
        ans.append(root.val)
        
        while True:
            
            if stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
                visited.add(stack[-1])
                ans.append(stack[-1].val)
                
            elif stack[-1].right and stack[-1].right not in visited:
                stack.append(stack[-1].right)
                visited.add(stack[-1])
                ans.append(stack[-1].val)
                
            elif stack[-1] in visited:
                stack.pop()
                
            if not stack:
                break
        
        return ans
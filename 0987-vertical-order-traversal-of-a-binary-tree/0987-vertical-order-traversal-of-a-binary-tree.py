# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)
        
        def dfs(node,row,col):
            if not node:
                return
            
            columns[col].append((row,node.val))
            
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
            return
        
        dfs(root,0,0)
        
        result = []
        
        for key,array in sorted(columns.items()):
            temp = [val for row,val in sorted(array)]
            result.append(temp)
     
        return result
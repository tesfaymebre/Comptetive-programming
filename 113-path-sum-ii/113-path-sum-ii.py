# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(node,path,path_sum):
            if not node:
                return
            path.append(node.val)
            path_sum += node.val
            
            if not node.left and not node.right:
                if path_sum == targetSum:
                    ans.append(path[:])
                
                path_sum -= path.pop()
                return
            
            dfs(node.left,path, path_sum)
            dfs(node.right,path, path_sum)
            path.pop()
            
            
        dfs(root,[],0)
        return ans
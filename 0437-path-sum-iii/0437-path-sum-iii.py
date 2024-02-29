# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        count = 0
        
        def dfs(node,prefix_sum):
            nonlocal count
            
            if not node:
                return 
            
            prefix_sum += node.val
            
            count += freq[prefix_sum - targetSum]
            freq[prefix_sum] += 1
            
            dfs(node.left, prefix_sum)
            dfs(node.right, prefix_sum)
            
            freq[prefix_sum] -= 1
            
            return
        
        dfs(root,0)
        
        return count
            
            
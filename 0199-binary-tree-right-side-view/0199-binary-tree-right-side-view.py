# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_most_node = defaultdict(int)
        
        def dfs(node, depth):
            if not node:
                return 
            
            right_most_node[depth] = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
            return
        
        dfs(root,0)
        
        result = []
        
        for depth in range(len(right_most_node)):
            result.append(right_most_node[depth])
            
        return result
        
            
            
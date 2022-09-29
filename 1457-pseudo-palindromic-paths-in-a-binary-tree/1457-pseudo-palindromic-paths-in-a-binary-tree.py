# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.paths = 0
        freq = [0]*10
        
        def dfs(node,freq):
            if not node.left and not node.right:
                odd_freq = 0
                
                for i in range(len(freq)):
                    if freq[i] % 2:
                        odd_freq += 1
                        
                if odd_freq <= 1:
                    self.paths += 1
                    
                return
            
            if node.left:
                freq[node.left.val] += 1
                dfs(node.left,freq)
                freq[node.left.val] -= 1
                
            if node.right:
                freq[node.right.val] += 1
                dfs(node.right,freq)
                freq[node.right.val] -= 1
                
        freq[root.val] += 1
        dfs(root,freq)
        return self.paths
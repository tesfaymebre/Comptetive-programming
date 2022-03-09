"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def dfs(par, d):
            if not par.children:
                self.depth = max(self.depth, d + 1)
                return
        
            for child in par.children:
                dfs(child, d + 1)
        
        self.depth = 0    
        dfs(root,0)
        
        return self.depth
        
        
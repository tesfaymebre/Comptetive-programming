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
            
        def dfs(par):
            if not par.children:
                return 1
        
            return max(1 + dfs(child) for child in par.children)
            
        return dfs(root)
        
        
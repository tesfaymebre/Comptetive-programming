# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        def countDistance(node, dicts):
            if not node:
                return  float('inf')
            if node == target:
                dicts[node] = 0
                return 0
            left = countDistance(node.left, dicts)
            right = countDistance(node.right, dicts)
            
            minn = min(left, right) - 1
            if minn != float('inf'):
                dicts[node] = minn
            
            return minn
        
        def find(node, k, visited):
            if not node:
                return None
            if k < 0:
                return None
            if k == 0:
                ans.append(node.val)
            if node.left not in visited:
                find(node.left, k - 1, visited)
            if node.right not in visited:
                find(node.right, k - 1, visited)
        
        visited = {}
        countDistance(root, visited)
        for node in visited:
            find(node, k + visited[node], visited)
        
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        
        def find(node, k, visited):
            if not node or k < 0:
                return None
            if k == 0:
                ans.append(node.val)
            if node.left not in visited:
                find(node.left, k - 1, visited)
            if node.right not in visited:
                find(node.right, k - 1, visited)

        def countDistance(node, visited):
            if not node:
                return  float('inf')
            
            if node == target:
                visited.add(node)
                find(node, k, visited)
                return 0

            left = countDistance(node.left, visited)
            right = countDistance(node.right, visited)
            
            minn = min(left, right) - 1
            if minn != float('inf'):
                visited.add(node)
                find(node, k + minn, visited)

            return minn
        

        countDistance(root, set())
        return ans
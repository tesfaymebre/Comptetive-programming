# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        
        def find(node, k, prev):
            if not node or k < 0:
                return None
            if k == 0:
                ans.append(node.val)
            if node.left != prev:
                find(node.left, k - 1, prev)
            if node.right != prev:
                find(node.right, k - 1, prev)

        def countDistance(node, visited):
            if not node:
                return  [None, float('inf')]
            
            if node == target:
                find(node, k, visited)
                return [node, 0]

            p, left = countDistance(node.left, visited)
            p2, right = countDistance(node.right, visited)
            
            n = None
            minn = min(left, right) - 1
            if left < right:
                n = p
            else:
                n = p2
        
            if minn != float('inf'):
                find(node, k + minn, n)

            return [node, minn]
        

        countDistance(root, None)
        return ans
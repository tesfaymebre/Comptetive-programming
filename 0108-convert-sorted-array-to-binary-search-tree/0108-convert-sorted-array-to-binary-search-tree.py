# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BST(left,right):
            if left > right:
                return None
            
            if left == right:
                return TreeNode(nums[left])
            
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            node.left = BST(left,mid-1)
            node.right = BST(mid+1,right)
            
            return node
        
        return BST(0,len(nums)-1)
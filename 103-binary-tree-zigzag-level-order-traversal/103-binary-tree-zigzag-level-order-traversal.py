# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        left_q = []
        right_q = []
        ans = []
        
        if not root:
            return ans
        
        left_q.append(root)
        ans.append([root.val])
        level = 0
        print(ans[level])
        while left_q or right_q:
            n = 0
            level += 1 
            ans_list = []
            
            if level %2 == 0:
                n = len(right_q)
                for j in range(n):
                    curr = right_q.pop()
                    if curr.left:
                        left_q.append(curr.left) 
                        ans_list.append(curr.left.val)
                    if curr.right:
                        left_q.append(curr.right) 
                        ans_list.append(curr.right.val)
            else:
                n = len(left_q)
                for i in range(n):
                    curr = left_q.pop()
                    if curr.right:
                        right_q.append(curr.right)
                        print(level, ans)
                        ans_list.append(curr.right.val)
                    if curr.left:
                        right_q.append(curr.left) 
                        ans_list.append(curr.left.val)
                        
            if ans_list:
                ans.append(ans_list) 
                
        return ans
               
                
        
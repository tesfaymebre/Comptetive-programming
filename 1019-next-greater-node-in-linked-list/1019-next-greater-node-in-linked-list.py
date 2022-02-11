# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nodes_val = []
        
        while head:
            nodes_val.append(head.val)
            head = head.next
            
        ans = [0]*len(nodes_val)
        stack = []
        
        for i in range(len(nodes_val)):
            
            while stack and nodes_val[stack[-1]] < nodes_val[i]:
                ans[stack.pop()] = nodes_val[i]
                
            stack.append(i)
            
        return ans
                
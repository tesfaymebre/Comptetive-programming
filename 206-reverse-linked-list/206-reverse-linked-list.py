# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        stack = []
        point = head
        
        while point:
            stack.append(point)
            point = point.next
            
        new_head = stack.pop()
        pre_node = new_head
        
        while stack:
            node = stack.pop()
            pre_node.next = node
            pre_node = node
        
        pre_node.next = None
        return new_head
        
        
        
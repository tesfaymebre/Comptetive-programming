# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        stack = []
        new_head = head
        dummy = head
        pos = 1
        curr = ListNode()
        
        while pos != left:
            curr = dummy
            dummy = dummy.next
            pos += 1
        
        while pos <= right:
            stack.append(dummy)
            if not dummy.next:
                dummy = None
                break
            
            dummy = dummy.next
            pos += 1
        
        if left == 1:
            new_head = stack[-1]
        
        while stack:
            node = stack.pop()
            
            if curr:
                curr.next = node
            curr = node
            
        curr.next = dummy
        
        return new_head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def cycleDetect(self,head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return fast
    
        return None
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = self.cycleDetect(head)
        if not node:
            return None
        
        slow = head
        while slow != node:
            slow = slow.next
            node = node.next
            
        return node
            
        
        
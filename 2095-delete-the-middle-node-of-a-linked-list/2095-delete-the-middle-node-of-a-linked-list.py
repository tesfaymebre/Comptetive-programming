# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        if not fast.next:
            slow.val = slow.next.val
            slow.next = slow.next.next
        else:
            slow.next = slow.next.next
            
        return head
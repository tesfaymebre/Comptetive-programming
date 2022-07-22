# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode()
        curr_before = before
        after = ListNode()
        curr_after = after
        
        while head:
            if head.val < x:
                curr_before.next = head
                curr_before = curr_before.next
            else:
                curr_after.next = head
                curr_after = curr_after.next

            head = head.next
        
        curr_after.next = None
        curr_before.next = after.next
        
        return before.next
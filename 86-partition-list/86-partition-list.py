# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        before = None
        curr_before = before
        after = None
        curr_after = after
        
        while head:
            if head.val < x:
                if not before:
                    before = head
                    
                    curr_before = before
                else:
                    curr_before.next = head
                    curr_before = curr_before.next
            else:
                if not after:
                    after = head
                    curr_after = after
                else:
                    curr_after.next = head
                    curr_after = curr_after.next

            head = head.next
        
        if curr_after and curr_before:
            curr_before.next = after
            curr_after.next = None
            return before
        elif not curr_before:
            curr_after.next = None
            return after
        else:
            curr_before.next = None
            return before
        
        
        return before
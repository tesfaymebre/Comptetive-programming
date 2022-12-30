# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        prev = None
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
       
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        
        forward = slow
        backward = prev
       
        if not fast.next and fast != backward:
            backward = backward.next
        
        while forward and backward:
            if forward.val != backward.val:
                return False
            
            forward = forward.next
            backward = backward.next
            
        return True
            
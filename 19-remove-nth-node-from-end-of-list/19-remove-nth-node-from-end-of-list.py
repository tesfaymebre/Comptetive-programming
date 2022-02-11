# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head
        count = 0
        
        while ptr1:
            ptr1 = ptr1.next
            count += 1
            
        if count == 1:
            head = None
            return head
        
        if count == n:
            ptr2 = ptr2.next
            head = ptr2
            return head
        
        for i in range(count-n -1):
            ptr2 = ptr2.next
        
        if  ptr2.next:    
            ptr2.next = ptr2.next.next
        else:
            ptr2.next = None
            
        return head
        
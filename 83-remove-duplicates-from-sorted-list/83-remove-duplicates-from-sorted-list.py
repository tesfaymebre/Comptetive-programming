# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        ptr1 = head
        ptr2 = ptr1
        
        while ptr1:
            if ptr1.next:
                ptr1 = ptr1.next
                
                if ptr2.val != ptr1.val:
                    ptr2.next = ptr1
                    ptr2 = ptr2.next
            else:
                ptr2.next = None
                return head
            
           
                
            
                
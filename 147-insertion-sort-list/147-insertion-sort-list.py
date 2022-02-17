# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = ListNode()
        ptr1.next = head
        
        while head.next:
            
            current = head.next
            temp = ptr1
            
            while temp.next is not current and temp.next.val<=current.val:
                temp=temp.next   
            
            if temp.next is current:
                head = head.next
            else:
                head.next = current.next
                current.next = temp.next
                temp.next = current
                
        return ptr1.next
            
                    
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        while head:
            head = head.next
            if head:
                head = head.next
                pointer = pointer.next

        return pointer
    
    
#         length = 0
#         pointer = head
        
#         while(head):
#             head = head.next
#             length +=1
            
#         middle = (length//2)
        
#         while(middle):
#             pointer = pointer.next
#             middle -=1
        
#         return pointer

            
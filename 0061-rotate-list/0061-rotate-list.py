# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        temp = head
        num_nodes = 0
        tail = head
        
        while temp:
            num_nodes += 1
            tail = temp
            temp = temp.next
        
        k %= num_nodes
        
        temp = head
        traverse = num_nodes - k - 1
        
        while traverse:
            temp = temp.next
            traverse -= 1
            
        tail.next = head
        new_head = temp.next
        temp.next = None
        
        return new_head
            
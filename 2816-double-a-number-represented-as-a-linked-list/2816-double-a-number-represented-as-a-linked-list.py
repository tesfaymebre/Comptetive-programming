# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        carry = 0
        curr = prev
        prev = None
      
        while curr:
            product = curr.val * 2 + carry
            carry = product // 10
            val = product % 10
            
            temp = curr.next
            curr.val = val
            curr.next = prev
            prev = curr
            curr = temp
            
        if carry:
            node = ListNode(carry)
            node.next = prev
            prev = node
            
        return prev
        
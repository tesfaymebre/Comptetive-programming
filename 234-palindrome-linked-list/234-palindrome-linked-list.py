# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack = []
        point = head
        
        while point:
            stack.append(point.val)
            point = point.next
        i = 0
        j = len(stack) -1
        
        while i <= j:
            
            if stack[i] != stack[j]:
                return False
            
            j -= 1
            i += 1
            
        return True
            
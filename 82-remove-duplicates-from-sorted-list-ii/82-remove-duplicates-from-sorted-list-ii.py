# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: 
            return head 
        
        ptr1 = head 
        ptr2 = None 
        curr = head.next
        flag = False 
        
        while curr: 
            
            if ptr1.val == curr.val: 
                curr = curr.next
                flag = True
                continue
			
            if not flag: 
                ptr2 = ptr1
                ptr1 = ptr1.next
                curr = curr.next
                continue
			
            flag = False
			
            if ptr2:
                ptr2.next = curr
                ptr1 = curr
            else:
                head = curr
                ptr1 = head
            curr = ptr1.next
		
        if flag:
            if ptr1 == head: 
                return None
            if ptr2: 
                ptr2.next = curr
                
        return head
        
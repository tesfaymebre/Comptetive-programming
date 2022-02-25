# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        if k <= 1:
            return head

        if head == None:
            return head

        new_node = ListNode(0)
        new_node.next = head

        length = 0
        ptr1 = head

        while ptr1:
            ptr1 = ptr1.next
            length += 1

        if length < k:
            return head

        m = length//k
        ptr2 = new_node
        ptr3 = ptr2 .next
        ptr4 = ptr2.next.next

        while m > 0:
            count = k-1

            while count >0:
                temp = ptr4.next
                ptr4.next=ptr3
                ptr3 = ptr4
                ptr4 = temp
                count -=1

            temp = ptr2 .next
            ptr2.next = ptr3
            temp.next = ptr4

            if m - 1 > 0:
                ptr2 = temp
                ptr3 = ptr4
                ptr4 = ptr3.next

            m -= 1

        return new_node.next
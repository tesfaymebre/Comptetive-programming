# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        base_size = n//k
        remainder = n%k

        result = []
        current = head

        for i in range(k):
            part_head = current
            part_size = base_size + 1 if i < remainder else base_size

            if part_head:
                for j in range(part_size - 1):
                    current = current.next

                next_head = current.next
                current.next = None
                current = next_head

            result.append(part_head)

        return result

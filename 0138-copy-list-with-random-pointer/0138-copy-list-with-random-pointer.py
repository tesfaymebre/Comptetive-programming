"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}
        prev = None
        node = head
        
        while node:
            if node not in dic:
                dic[node] = Node(node.val, node.next, node.random)
                
            if prev:
                prev.next = dic[node]
            else:
                head = dic[node]
                
            if node.random:
                if node.random not in dic:
                    dic[node.random] = Node(node.random.val, node.random.next, node.random.random)
                dic[node].random = dic[node.random]
            prev = dic[node]
            node = node.next
            
        return head
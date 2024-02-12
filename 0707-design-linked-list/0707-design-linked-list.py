class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        idx = 0
        curr = self.head
        while idx < index:
            curr = curr.next
            idx += 1
            
        return curr.val       

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        
        if self.head.val == -1:
            self.head = new_head
            self.tail = self.head
        else:
            new_head.next = self.head
            self.head = new_head
            
        self.size += 1
       

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)
        
        if self.tail.val == -1:
            self.head = new_tail
            self.tail = self.head
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        if index > self.size:
            return
        
        idx = 0
        curr = self.head
        new_node = Node(val)
        
        while idx < index-1:
            curr = curr.next
            idx += 1
            
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            
            if not self.head:
                self.head = Node(-1)
                self.tail = self.head
                
            return
        
        idx = 0
        curr = self.head
        
        while idx < index-1:
            curr = curr.next
            idx += 1
        
        curr.next = curr.next.next
        
        if index == self.size - 1:
            self.tail = curr
        
        self.size -= 1
        
        if self.size == 1:
            self.head = self.tail
            
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
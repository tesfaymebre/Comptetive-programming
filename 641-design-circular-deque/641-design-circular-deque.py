class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.stack = []

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.stack.append(value)
        else:
            temp = []
            
            while self.stack:
                temp.append(self.stack.pop())
            
            self.stack.append(value)
            
            while temp:
                self.stack.append(temp.pop())
        
        return True
            

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.stack.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            temp = []
            
            while self.stack:
                temp.append(self.stack.pop())
            
            temp.pop()
            
            while temp:
                self.stack.append(temp.pop())
            
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.stack.pop()
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.stack[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.stack[-1]

    def isEmpty(self) -> bool:
        if not self.stack:
            return True
        
        return False

    def isFull(self) -> bool:
        if len(self.stack) == self.k:
            return True
        
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
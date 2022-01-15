class MyQueue:

    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack)):
            self.queue.append(self.stack.pop())
        temp = self.queue.pop()

        for j in range(len(self.queue)):
            self.stack.append(self.queue.pop())
        return temp

    def peek(self) -> int:
        for i in range(len(self.stack)):
            self.queue.append(self.stack.pop())
        temp = self.queue.pop()
        self.queue.append(temp)

        for j in range(len(self.queue)):
            self.stack.append(self.queue.pop())
        return temp

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

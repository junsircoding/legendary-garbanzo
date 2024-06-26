class MyQueue:

    def __init__(self):
        self.stack_input = []
        self.stack_output = []

    def in_to_out(self):
        while self.stack_input[::-1]:
            self.stack_output.insert(0, self.stack_input.pop(0))

    def push(self, x: int) -> None:
        self.stack_input.append(x)

    def pop(self) -> int:
        self.in_to_out()
        val = self.stack_output.pop()
        return val

    def peek(self) -> int:
        self.in_to_out()
        if not self.empty():
            return self.stack_output[-1]
        else:
            return None

    def empty(self) -> bool:
        self.in_to_out()
        if len(self.stack_output) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
#param_3 = obj.peek()
#param_4 = obj.empty()

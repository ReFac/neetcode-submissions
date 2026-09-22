class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mstack:
            self.mstack.append(val)
        else:
            curr = self.mstack[-1]
            self.mstack.append(curr if curr < val else val)

    def pop(self) -> None:
        self.mstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]
        

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_num) == 0:
            self.min_num = [val]
        elif self.min_num[-1] >= val:
            self.min_num.append(val)
            
    def pop(self) -> None:
        if self.stack.pop() == self.min_num[-1]:
            self.min_num.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num[-1]

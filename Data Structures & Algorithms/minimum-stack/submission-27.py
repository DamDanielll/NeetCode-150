class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []
        
    def push(self, val: int) -> None:
        if self.mintop() == None:
            self.mins.append(val)
        elif self.mintop() >= val:
            self.mins.append(val)
        self.items.append(val)

    def pop(self) -> None:
        if self.top() == self.mintop():
            self.mins.pop()
        return self.items.pop()

    def top(self) -> int:
        if not self.items:
            return
        return self.items[-1]

    def mintop(self) -> int:
        if not self.mins:
            return
        return self.mins[-1]

    def getMin(self) -> int:
        return self.mintop()

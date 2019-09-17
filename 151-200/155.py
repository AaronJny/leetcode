class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_pos = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.min_pos:
            self.min_pos.append(0)
        else:
            if self.data[self.min_pos[-1]] >= x:
                self.min_pos.append(len(self.data)-1)
            else:
                self.min_pos.append(self.min_pos[-1])

    def pop(self) -> None:
        self.data.pop()
        self.min_pos.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.data[self.min_pos[-1]]
MX = 1000005


class Stack:

    def __init__(self):
        self.dat = [0 for _ in range(MX)]
        self.pos = 0

    def push(self, x):
        self.dat[self.pos] = x
        self.pos += 1

    def pop(self):
        self.pos -= 1
        return self.dat[self.pos]

    def top(self):
        return self.dat[self.pos - 1]

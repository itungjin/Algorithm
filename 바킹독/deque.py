MX = 1000005


class deque:
    def __init__(self):
        self.dat = [0 for _ in range(2*MX + 1)]
        self.head, self.tail = MX, MX

    def push_front(self, x):
        self.head -= 1
        self.dat[self.head] = x

    def push_back(self, x):
        self.dat[self.tail] = x
        self.tail += 1

    def pop_front(self):
        self.head += 1

    def pop_back(self):
        self.tail -= 1

    def front(self):
        return self.dat[self.head]

    def back(self):
        return self.dat[self.tail - 1]

    def test(self):
        self.push_back(30)
        print(self.front())
        print(self.back())
        self.push_front(25)
        self.push_back(12)
        print(self.back())
        self.push_back(62)
        self.pop_front()
        print(self.front())
        self.pop_front()
        print(self.back())


if __name__ == '__main__':
    d = deque()
    d.test()

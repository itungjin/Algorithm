MX = 1000005


class queue:
    def __init__(self):
        self.__dat = [0 for _ in range(MX)]
        self.__head = 0
        self.__tail = 0

    def push(self, x):
        self.__dat[self.__tail] = x
        self.__tail += 1

    def pop(self):
        self.__head += 1

    def front(self):
        return self.__dat[self.__head]

    def back(self):
        return self.__dat[self.__tail - 1]

    def test(self):
        self.push(10)
        self.push(20)
        self.push(30)
        print(self.front())
        print(self.back())
        self.pop()
        self.pop()
        self.push(15)
        self.push(25)
        print(self.front())
        print(self.back())


if __name__ == "__main__":
    q = queue()
    q.test()

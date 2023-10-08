import sys
input = sys.stdin.readline

MAX_SIZE = 100005


class Heap:
    def __init__(self):
        self.__heap = [0] * MAX_SIZE
        self.__size = 0

    def push(self, x: int):
        self.__size += 1
        self.__heap[self.__size] = x
        now_node = self.__size
        mother_node = now_node // 2
        while mother_node != 0 and self.__heap[now_node] < self.__heap[mother_node]:
            self.__heap[now_node], self.__heap[mother_node] = self.__heap[mother_node], self.__heap[now_node]
            now_node, mother_node = mother_node, mother_node // 2

    def top(self) -> int:
        if self.__size == 0:
            return 0
        else:
            return self.__heap[1]

    def pop(self):
        if self.__size == 0:
            return
        if self.__size == 1:
            self.__size -= 1
            return
        self.__heap[1], self.__heap[self.__size] = self.__heap[self.__size], self.__heap[1]
        self.__size -= 1
        parent = 1
        left_child = parent * 2
        right_child = left_child + 1
        while left_child <= self.__size:
            min_child = left_child
            if right_child <= self.__size and self.__heap[left_child] > self.__heap[right_child]:
                min_child = right_child
            if self.__heap[parent] > self.__heap[min_child]:
                self.__heap[parent], self.__heap[min_child] = self.__heap[min_child], self.__heap[parent]
                parent = min_child
                left_child = 2 * parent
                right_child = left_child + 1
            else:
                break


N = int(input().rstrip())
heap = Heap()
for _ in range(N):
    x = int(input().rstrip())
    if x > 0:
        heap.push(x)
    elif x == 0:
        print(heap.top())
        heap.pop()


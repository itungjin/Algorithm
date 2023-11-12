MAX_SIZE = 100005


# 최소 힙
class Heap:
    def __init__(self):
        self.__heap = [0] * MAX_SIZE
        self.__size = 0

    def push(self, x: int):
        self.__size += 1
        self.__heap[self.__size] = x
        child = self.__size
        parent = child // 2
        while parent != 0 and self.__heap[child] < self.__heap[parent]:
            self.__heap[child], self.__heap[parent] = self.__heap[parent], self.__heap[child]
            child, parent = parent, parent // 2

    def top(self) -> int:
        if self.__size == 0:
            return None
        else:
            return self.__heap[1]

    def pop(self):
        if self.__size == 0:
            return
        self.__heap[1], self.__heap[self.__size] = self.__heap[self.__size], self.__heap[1]
        self.__size -= 1
        parent = 1
        while parent * 2 <= self.__size:
            left_child = 2 * parent
            right_child = left_child + 1

            min_child = left_child
            if right_child <= self.__size and self.__heap[left_child] > self.__heap[right_child]:
                min_child = right_child
            if self.__heap[parent] <= self.__heap[min_child]:
                break
            self.__heap[parent], self.__heap[min_child] = self.__heap[min_child], self.__heap[parent]
            parent = min_child

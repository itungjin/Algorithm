# 연결리스트

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.tail = Node(1, None)
        self.tail.next = self.tail
        self.curr = self.tail

    def traversal(self):
        self.curr = self.curr.next

    def insert(self, value):
        new_item = Node(value, self.tail.next)
        self.tail.next = new_item
        self.tail = new_item

    def delete(self):
        print(self.curr.next.item, end='')
        self.curr.next = self.curr.next.next

    def delete_last(self):
        print(self.curr.item, end='')


N, K = map(int, input().split())

peoples = [(i+1) for i in range(N)]

peoples_list = CircularLinkedList()
for i in range(1, N):
    peoples_list.insert(peoples[i])
peoples_list.curr = peoples_list.tail

print('<', end='')
for i in range(N-1):
    for j in range(K-1):
        peoples_list.traversal()
    peoples_list.delete()
    print(end=', ')
peoples_list.delete_last()
print('>')

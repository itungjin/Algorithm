# 큐

from collections import deque

N = int(input())


def card():
    if N == 1:
        return (1)

    q = deque()
    for i in range(1, N+1):
        q.append(i)

    q.popleft()
    while len(q) != 1:
        q.append(q.popleft())
        q.popleft()
    return (q.pop())


print(card())

# 덱

from collections import deque

N, M = map(int, input().split())
dq = deque([i for i in range(1, N+1)])
numbers = list(map(int, input().split()))

answer = 0
for number in numbers:
    length = len(dq)
    move = 0
    while dq[0] != number:
        dq.append(dq.popleft())
        move += 1
    dq.popleft()
    answer += min(move, length - move)

print(answer)

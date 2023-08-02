from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

deq = deque([(A[0], 0)])
print(A[0], end=' ')
for i in range(1, L):
    while deq and deq[len(deq) - 1][0] >= A[i]:
        deq.pop()
    deq.append((A[i], i))
    print(deq[0][0], end=' ')
for i in range(L, N):
    while deq and deq[len(deq) - 1][0] >= A[i]:
        deq.pop()
    while deq and deq[0][1] < i-L+1:
        deq.popleft()
    deq.append((A[i], i))
    print(deq[0][0], end=' ')

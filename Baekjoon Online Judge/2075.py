import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
heap = list()
divisor = 1
for i in range(N, 0, -1):
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    while i == N // (divisor + 1):
        divisor += 1
    for j in range(divisor):
        heapq.heappush(heap, -a[j])
for i in range(N - 1):
    heapq.heappop(heap)
print(-heapq.heappop(heap))

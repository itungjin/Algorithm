import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
heapq.heapify(a)
for i in range(m):
    x, y = heapq.heappop(a), heapq.heappop(a)
    heapq.heappush(a, x + y)
    heapq.heappush(a, x + y)
print(sum(a))

import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
heap = []
row = list(map(int, input().split()))
row.sort()
for number in row:
    heapq.heappush(heap, number)
for _ in range(N - 1):
    row = list(map(int, input().split()))
    row.sort(reverse=True)
    for number in row:
        if number < heap[0]:
            break
        heapq.heappushpop(heap, number)
print(heapq.heappop(heap))

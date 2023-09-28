import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
l = [list(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x: (x[0], x[1]))
answer = 1
heap = []
for s, t in l:
    if len(heap) < answer:
        heapq.heappush(heap, t)
    else:
        if s < heap[0]:
            answer += 1
            heapq.heappush(heap, t)
        else:
            heapq.heappushpop(heap, t)
print(answer)

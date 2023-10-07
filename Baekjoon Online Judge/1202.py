import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewel = []
bag = []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jewel, (M, V))
for _ in range(K):
    C = int(input().rstrip())
    heapq.heappush(bag, C)
answer = 0
popped_jewel = []
while bag:
    c = heapq.heappop(bag)
    if not jewel and not popped_jewel:
        break
    else:
        while jewel and jewel[0][0] <= c:
            _, v = heapq.heappop(jewel)
            heapq.heappush(popped_jewel, -v)
        if not popped_jewel:
            continue
        answer -= heapq.heappop(popped_jewel)
print(answer)

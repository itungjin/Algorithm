import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    K = int(input().rstrip())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    cost = 0
    while len(files) != 1:
        f1, f2 = heapq.heappop(files), heapq.heappop(files)
        f3 = f1 + f2
        cost += f3
        heapq.heappush(files, f3)
    print(cost)
import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
h = []
for _ in range(N):
    d, c = list(map(int, input().split()))
    heapq.heappush(h, (-d, c))
h_solvable = []
answer = 0
for time in range(-h[0][0], 0, -1):
    while h and time == -h[0][0]:
        heapq.heappush(h_solvable, -heapq.heappop(h)[1])
    if h_solvable:
        answer -= heapq.heappop(h_solvable)
print(answer)
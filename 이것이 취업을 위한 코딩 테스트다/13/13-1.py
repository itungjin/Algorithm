# BFS
import sys
from collections import deque

input = sys.stdin.readline
INF = 1e9

# 도시의 개수 2 <= n <= 300000
# 도로의 개수 1 <= m <= 1000000
# 거리 정보 1 <= k <= 300000
# 출발 도시 1 <= x <= n
n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)

answer = []
distance = [INF] * (n + 1)

# a = x
# distance[a] = 0
# queue = deque()
# for b in roads[a]:
#     queue.append(b)
#     distance[b] = 1
# 위와 같이 하면 틀림(백준)

distance[x] = 0
queue = deque([x])

while queue:
    a = queue.popleft()
    if distance[a] == k:
        answer.append(a)
    elif distance[a] > k:
        break
    for b in roads[a]:
        if distance[b] == INF:
            queue.append(b)
            distance[b] = distance[a] + 1
answer.sort()

if answer:
    for city in answer:
        print(city)
else:
    print(-1)

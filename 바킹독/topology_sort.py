from collections import deque

graph = [[] for _ in range(8)]
graph[1] = [2]
graph[3] = [2, 4]
graph[4] = [2, 5]
graph[5] = [6]
graph[7] = [5]
indegree = [0] * 8
indegree[2] = 3
indegree[4] = 1
indegree[5] = 2
indegree[6] = 1


def topology_sort():
    q = deque()
    for i in range(1, 8):
        if indegree[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for u in graph[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                q.append(u)


topology_sort()

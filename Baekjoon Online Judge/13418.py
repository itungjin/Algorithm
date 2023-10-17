import sys

input = sys.stdin.readline

N, M = map(int, input().split())

entrance = list(map(int, input().split()))[2]
if entrance == 1:
    entrance = 0
else:
    entrance = 1
edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    if C == 1:
        C = 0
    else:
        C = 1
    edges.append((C, A, B))
edges.sort()
parent = [i for i in range(N + 1)]


def find_parent(v1):
    if parent[v1] == v1:
        return v1
    parent[v1] = find_parent(parent[v1])
    return parent[v1]


def have_same_parent(v1, v2):
    pv1 = find_parent(v1)
    pv2 = find_parent(v2)
    if pv1 == pv2:
        return True
    else:
        if pv1 > pv2:
            parent[pv1] = pv2
        else:
            parent[pv2] = pv1
        return False


worst = entrance
cnt = 1
for cost, v1, v2 in edges:
    if not have_same_parent(v1, v2):
        worst += cost
        cnt += 1
    if cnt == N:
        break

parent = [i for i in range(N + 1)]
best = entrance
cnt = 1
for i in range(M - 1, -1, -1):
    cost, v1, v2 = edges[i]
    if not have_same_parent(v1, v2):
        best += cost
        cnt += 1
    if cnt == N:
        break
print(best ** 2 - worst ** 2)

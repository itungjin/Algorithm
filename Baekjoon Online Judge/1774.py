import sys

input = sys.stdin.readline

N, M = map(int, input().split())

loc = [() for _ in range(N + 1)]
for i in range(1, N + 1):
    X, Y = map(int, input().split())
    loc[i] = (X, Y)

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


cnt = 0
for _ in range(M):
    v1, v2 = map(int, input().split())
    if not have_same_parent(v1, v2):
        cnt += 1
edges = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        edges.append((((loc[j][0] - loc[i][0]) ** 2 + (loc[j][1] - loc[i][1]) ** 2) ** 0.5, i, j))
edges.sort()
ans = 0
for dist, v1, v2 in edges:
    if not have_same_parent(v1, v2):
        cnt += 1
        ans += dist
    if cnt == N - 1:
        break
print(f'{ans:.2f}')

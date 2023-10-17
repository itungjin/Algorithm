import sys

input = sys.stdin.readline

N = int(input().rstrip())
edges = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(i + 1, N):
        edges.append((tmp[j], i, j))
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


ans = 0
cnt = 0
for cost, v1, v2 in edges:
    if not have_same_parent(v1, v2):
        ans += cost
        cnt += 1
    if cnt == N - 1:
        break
print(ans)

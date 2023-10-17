import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
power_plants = set(map(int, input().split()))
cabels = [[] for _ in range(M)]
for i in range(M):
    u, v, w = map(int, input().split())
    cabels[i] = (w, u, v)
cabels.sort()
parent = [i for i in range(N + 1)]


def find_parent(v):
    if parent[v] == v:
        return v
    parent[v] = find_parent(parent[v])
    return parent[v]


def can_union(v1, v2):
    pv1 = find_parent(v1)
    pv2 = find_parent(v2)
    if pv1 in power_plants and pv2 in power_plants:
        return False
    elif pv1 in power_plants:
        parent[pv2] = pv1
    elif pv2 in power_plants:
        parent[pv1] = pv2
    else:
        if pv1 == pv2:
            return False
        elif pv1 > pv2:
            parent[pv1] = pv2
        else:
            parent[pv2] = pv1
    return True


ans = 0
cnt = 0
for w, u, v in cabels:
    if can_union(u, v):
        ans += w
        cnt += 1
    if cnt == N - K:
        break
print(ans)

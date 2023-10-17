import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = [[] for _ in range(E)]
for i in range(E):
    A, B, C = map(int, input().split())
    edges[i] = (C, A, B)
parent = [i for i in range(V + 1)]


def find_parent(v):
    if parent[v] == v:
        return v
    parent[v] = find_parent(parent[v])
    return parent[v]


def union(v1, v2):
    vp1 = find_parent(v1)
    vp2 = find_parent(v2)
    if vp1 < vp2:
        parent[vp2] = vp1
    else:
        parent[vp1] = vp2


def is_diff_group(v1, v2):
    if find_parent(v1) == find_parent(v2):
        return False
    else:
        return True


def kruskal():
    edges.sort()
    cnt_cost = 0
    cnt_edges = 0
    for cost, v1, v2 in edges:
        if is_diff_group(v1, v2):
            union(v1, v2)
            cnt_cost += cost
            cnt_edges += 1
        if cnt_edges == V - 1:
            return cnt_cost


print(kruskal())

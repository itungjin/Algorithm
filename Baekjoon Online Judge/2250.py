import sys
import math

input = sys.stdin.readline

N = int(input().rstrip())
parent = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(N):
    p, left, right = map(int, input().split())
    if left != -1:
        parent[left] = p
    if right != -1:
        parent[right] = p
    graph[p].append(left)
    graph[p].append(right)
for i in range(1, N + 1):
    if parent[i] == 0:
        root = i
        break

last = 1
w = [0] * (N + 1)
weights_in_h = [[] for _ in range(N + 1)]


def preorder(cur, h):
    global last
    if graph[cur][0] != -1:
        preorder(graph[cur][0], h + 1)
    w[cur] = last
    weights_in_h[h].append(last)
    last += 1
    if graph[cur][1] != -1:
        preorder(graph[cur][1], h + 1)


preorder(root, 1)
ans1, ans2 = 0, 0
for i in range(1, len(weights_in_h)):
    if weights_in_h[i]:
        weights_in_h[i].sort()
        tmp = weights_in_h[i][-1] - weights_in_h[i][0] + 1
        if tmp > ans2:
            ans2 = tmp
            ans1 = i
    else:
        break
print(ans1, ans2)

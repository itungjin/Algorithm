SIZE = 10

adj = [[] for _ in range(SIZE)]
p = [0] * SIZE
depth = [0] * SIZE


def dfs(root: int):
    s = [root]
    while s:
        cur = s.pop()
        print(cur, end=' ')
        for nxt in adj[cur]:
            if p[cur] == nxt:
                continue
            s.append(nxt)
            p[nxt] = cur
            depth[nxt] = depth[cur] + 1

p[2] = 1
p[5] = 2
p[3] = 1
p[4] = 1
p[6] = 4
p[7] = 6
p[8] = 6
adj[1] = [2, 3, 4]
adj[2] = [1, 5]
adj[3] = [1]
adj[4] = [1, 6]
adj[5] = [2]
adj[6] = [4, 7, 8]
adj[7] = [6]
adj[8] = [6]
dfs(1)
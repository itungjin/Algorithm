import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

M, N = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
print(maze)
heap = [(0, 0, 0)]
cnt = [[INF] * M for _ in range(N)]
moves = ((1, 0), (0, 1))
while heap:
    c, n, m = heapq.heappop(heap)
    if c != cnt[n][m]:
        continue
    for dn, dm in moves:
        nn = n + dn
        nm = m + dm
        if nn >= N or nm >= M:
            continue
        if c + maze[nn][nm] < cnt[nn][nm]:
            cnt[nn][nm] = c + maze[nn][nm]
            heapq.heappush(heap, (cnt[nn][nm], nn, nm))
print(cnt[N-1][M-1])

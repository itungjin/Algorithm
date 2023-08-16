import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split()) # 가로, 세로
tomatoes = [list(map(int, input().split())) for _ in range(N)]

is_available = True
for r in range(N):
    if 0 in tomatoes[r]:
        is_available = False
        break
if is_available:
    print(0)
else:
    day = -1
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    
    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 1:
                queue.append((r, c))

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    while queue:
        day += 1
        temp = list()
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and tomatoes[nr][nc] == 0:
                    tomatoes[nr][nc] = 1
                    temp.append((nr, nc))
        for r, c in temp:
            queue.append((r, c))
    
    is_available = True
    for r in range(N):
        if 0 in tomatoes[r]:
            is_available = False
            break
    
    if is_available:
        print(day)
    else:
        print(-1)
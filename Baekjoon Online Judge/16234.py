# BFS

from collections import deque

# N x N 크기의 땅이 있고, 땅은 1 X 1 개의 칸으로 나누어져 있다.
# 각각의 땅에는 나라가 하나씩 있고, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
# 인접한 나라 사이에는 국경선이 존재한다. 모든 나라의 크기는 1 X 1이므로 모든 국경선은 정사각형 형태이다.

# 1 <= N <= 50, N은 땅의 크기
# 1 <= L <= R <= 100, L <= 인구 차이 <= R이면 국경선을 연다.
N, L, R = map(int, input().split())
# 0 <= A[r][c] <= 100
A = [list(map(int, input().split())) for _ in range(N)]

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
answer = 0
while True:
    moved = False
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = True
                union = list()
                population = 0
                queue = deque([[r, c]])
                while queue:
                    _r, _c = queue.popleft()
                    union.append([_r, _c])
                    population += A[_r][_c]
                    for mr, mc in moves:
                        nr, nc = _r + mr, _c + mc
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and L <= abs(A[_r][_c] - A[nr][nc]) <= R:
                            moved = True
                            visited[nr][nc] = True
                            queue.append([nr, nc])
                for _r, _c in union:
                    A[_r][_c] = population // len(union)
    if moved:
        answer += 1
    else:
        break

print(answer)

# bfs

from collections import deque

INF = 1e9

n, m = map(int, input().split())  # 4 <= n, m <= 200
maze = [list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1


def bfs(maze, visited):
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue = deque([[1, 0], [0, 1]])
    visited[1][0] = 2
    visited[0][1] = 2
    while queue:
        r, c = queue.popleft()
        for move_r, move_c in moves:
            _r, _c = r + move_r, c + move_c
            if 0 <= _r < n and 0 <= _c < m:
                if maze[_r][_c] == 1 and visited[_r][_c] == 0:
                    visited[_r][_c] = visited[r][c] + 1
                    queue.append([_r, _c])


bfs(maze, visited)
print(visited[n - 1][m - 1])

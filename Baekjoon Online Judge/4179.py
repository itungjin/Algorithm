import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]
maze_fire = deepcopy(maze)
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
queue = deque()
queue_fire = deque()
for r in range(R):
    for c in range(C):
        if maze[r][c] == "F":
            maze_fire[r][c] = 1
            queue_fire.append((r, c))
        elif maze[r][c] == 'J':
            maze_fire[r][c] = '.'
            maze[r][c] = 1
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                for i in range(4):
                    nr, nc = row + dr[i], col + dc[i]
                    if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == '.':
                        maze[nr][nc] = maze[row][col] + 1
                        queue.append((nr, nc))
while queue_fire:
    r, c = queue_fire.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and maze_fire[nr][nc] == '.':
            maze_fire[nr][nc] = maze_fire[r][c] + 1
            queue_fire.append((nr, nc))


min_escape_time = 1e9
for r in range(R):
    if type(maze[r][0]) == int:
        if type(maze_fire[r][0]) == int:
            if maze[r][0] < maze_fire[r][0]:
                min_escape_time = min(min_escape_time, maze[r][0])
        else:
            min_escape_time = min(min_escape_time, maze[r][0])
    if type(maze[r][C-1]) == int:
        if type(maze_fire[r][C-1]) == int:
            if maze[r][C-1] < maze_fire[r][C-1]:
                min_escape_time = min(min_escape_time, maze[r][C-1])
        else:
            min_escape_time = min(min_escape_time, maze[r][C-1])
for c in range(C):
    if type(maze[0][c]) == int:
        if type(maze_fire[0][c]) == int:
            if maze[0][c] < maze_fire[0][c]:
                min_escape_time = min(min_escape_time, maze[0][c])
        else:
            min_escape_time = min(min_escape_time, maze[0][c])
    if type(maze[R-1][c]) == int:
        if type(maze_fire[R-1][c]) == int:
            if maze[R-1][c] < maze_fire[R-1][c]:
                min_escape_time = min(min_escape_time, maze[R-1][c])
        else:
            min_escape_time = min(min_escape_time, maze[R-1][c])
if min_escape_time == 1e9:
    print("IMPOSSIBLE")
else:
    print(min_escape_time)
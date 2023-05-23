# 구현
# 사과를 먹으면 뱀 길이 += 1
# 벽 또는 자기자신과 부딪히면 게임 끝
# NxN 정사각 보드 위에서 게임 진행, 벽은 상하좌우 끝에 존재
# 게임 시작시 뱀의 위치는 맨위 맨좌측, 길이는 1, 방향은 오른쪽
# 뱀이 이동시 길이 + 1, 머리가 늘어남
# 이동한 칸에 자기 자신이 있으면 게임 끝
# 이동한 칸에 사과가 있으면 그대로 이동 끝
# 이동한 칸에 사과가 없으면 길이 - 1, 꼬리가 없어짐
from collections import deque

n = int(input())  # 2 <= n <= 100 보드의 크기
k = int(input())  # 0 <= k <= 100 사과의 개수

# 사과의 위치
apples = [list(map(int, input().split())) for _ in range(k)]

l = int(input())  # 1 <= L <= 100 뱀의 방향 변환 횟수

# 방향 변환 정보
change_directions = [input().split() for _ in range(l)]

directions = ([0, 1], [1, 0], [0, -1], [-1, 0])
board = [[0] * n for _ in range(n)]
board[0][0] = 1
for apple in apples:
    board[apple[0] - 1][apple[1] - 1] = 2

direction = 0
snake = deque([[0, 0]])
head = [0, 0]
answer = 0
game_over = False

for second, next_direction in change_directions:
    while int(second) > answer:
        answer += 1
        head = [head[0] + directions[direction][0], head[1] + directions[direction][1]]
        if 0 <= head[0] < n and 0 <= head[1] < n:
            if board[head[0]][head[1]] == 1:
                game_over = True
                break
            else:
                if board[head[0]][head[1]] == 2:
                    board[head[0]][head[1]] = 1
                    snake.append([head[0], head[1]])
                else:
                    board[head[0]][head[1]] = 1
                    snake.append([head[0], head[1]])
                    tail = snake.popleft()
                    board[tail[0]][tail[1]] = 0
        else:
            game_over = True
            break
    if game_over:
        break

    if next_direction == 'D':
        direction = direction + 1 if direction != 3 else 0
    else:
        direction = direction - 1 if direction != 0 else 3

if game_over:
    print(answer)
else:
    while True:
        answer += 1
        head = [head[0] + directions[direction][0], head[1] + directions[direction][1]]
        if 0 <= head[0] < n and 0 <= head[1] < n:
            if board[head[0]][head[1]] == 1:
                game_over = True
                break
            else:
                if board[head[0]][head[1]] == 2:
                    board[head[0]][head[1]] = 1
                    snake.append([head[0], head[1]])
                else:
                    board[head[0]][head[1]] = 1
                    snake.append([head[0], head[1]])
                    tail = snake.popleft()
                    board[tail[0]][tail[1]] = 0
        else:
            game_over = True
            break
    print(answer)

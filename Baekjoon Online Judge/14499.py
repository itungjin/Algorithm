import sys

input = sys.stdin.readline

N, M, x, y, K = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
instructions = list(map(int, input().split()))
dice = [0] * 7
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
now_upper = 1
now_right = 3
now_front = 5

# 위가 1 아랜 6
# 위가 2 아랜 5
# 위가 3 아랜 4


for instruction in instructions:
    nx, ny = x + dx[instruction], y + dy[instruction]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    x, y = nx, ny
    if instruction == 1:
        now_upper, now_right = 7 - now_right, now_upper
    elif instruction == 2:
        now_upper, now_right = now_right, 7 - now_upper
    elif instruction == 3:
        now_upper, now_front = now_front, 7 - now_upper
    else:
        now_upper, now_front = 7 - now_front, now_upper

    if board[x][y] == 0:
        board[x][y] = dice[7 - now_upper]
    else:
        dice[7 - now_upper] = board[x][y]
        board[x][y] = 0
    print(dice[now_upper])

import sys

input = sys.stdin.readline

board = [[0] * 101 for _ in range(101)]
N = int(input().rstrip())
# x축 방향, y축 방향에 유의
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
move = [[0] for _ in range(11)]

# 시계방향
# 위쪽은 왼쪽으로1->2
# 오른쪽은 위쪽으로0->1
# 왼쪽은 아래쪽으로2->3
# 아래쪽은 오른쪽으로3->0
for i in range(1, 11):
    move[i] = move[i - 1][:]
    for j in range(len(move[i - 1]) - 1, -1, -1):
        move[i].append((move[i - 1][j] + 1) % 4)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1
    for direction in move[g]:
        direction = (direction + d) % 4
        x, y = x + dx[direction], y + dy[direction]
        board[y][x] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            answer += 1
print(answer)

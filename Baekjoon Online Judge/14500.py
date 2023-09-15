import sys

input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]


def turn(origin):
    new = [[0] * len(origin) for _ in range(len(origin))]
    for r in range(len(origin)):
        for c in range(len(origin)):
            new[c][len(origin) - 1 - r] = origin[r][c]
    return new


def flip_horizontal(origin):
    new = [[0] * len(origin) for _ in range(len(origin))]
    for r in range(len(origin)):
        for c in range(len(origin)):
            new[r][len(origin) - 1 - c] = origin[r][c]
    return new


tetromino = [[], [], [], [], []]
tetromino[0].append([
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])
tetromino[0].append(turn(tetromino[0][0]))
tetromino[1].append([
    [1, 1],
    [1, 1]
])
tetromino[2].append([
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 0]
])
tetromino[3].append([
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0]
])
tetromino[4].append([
    [1, 1, 1],
    [0, 1, 0],
    [0, 0, 0]
])
for j in range(3):
    tetromino[2].append(turn(tetromino[2][j]))
    tetromino[4].append(turn(tetromino[4][j]))
tetromino[3].append(turn(tetromino[3][0]))
for i in range(4):
    tetromino[2].append(flip_horizontal(tetromino[2][i]))
for i in range(2):
    tetromino[3].append(flip_horizontal(tetromino[3][i]))

size = [4, 2, 3, 3, 3]


def solution(tet, status, i, j):
    sum_num = 0
    for r in range(size[tet]):
        for c in range(size[tet]):
            if tetromino[tet][status][r][c] == 1:
                if r + i < 0 or r + i >= N or c + j < 0 or c + j >= M:
                    return 0
                else:
                    sum_num += paper[r + i][c + j]
    return sum_num


answer = 0
for tet in range(5):
    for status in range(len(tetromino[tet])):
        for i in range(1 - len(tetromino[tet][status]), N):
            for j in range(1 - len(tetromino[tet][status]), M):
                answer = max(answer, solution(tet, status, i, j))
print(answer)

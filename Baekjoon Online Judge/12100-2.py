from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def rotate(temp):
    _temp = deepcopy(temp)
    for r in range(N):
        for c in range(N):
            temp[r][c] = _temp[c][N - 1 - r]


def move(i, temp):
    for j in range(i):
        rotate(temp)
    for c in range(N):
        r1 = 0
        while r1 < N:
            if temp[r1][c] == 0:
                r1 += 1
                continue
            r2 = r1 + 1
            while r2 < N:
                if temp[r2][c] == 0:
                    r2 += 1
                    continue
                elif temp[r2][c] == temp[r1][c]:
                    temp[r1][c] *= 2
                    temp[r2][c] = 0
                    r1 = r2
                    break
                else:
                    r1 = r2 - 1
                    break
            r1 += 1

        r1 = 0
        while r1 < N:
            while r1 < N and temp[r1][c] != 0:
                r1 += 1
            r2 = r1 + 1
            while r2 < N and temp[r2][c] == 0:
                r2 += 1
            while r2 < N and temp[r2][c] != 0:
                temp[r1][c] = temp[r2][c]
                temp[r2][c] = 0
                r1 += 1
                r2 += 1
            if r2 == N:
                break


def solution(n, temp):
    global answer
    if n == 5:
        for i in range(N):
            answer = max(answer, max(temp[i]))
        return
    for i in range(4):
        a = deepcopy(temp)
        move(i, a)
        solution(n + 1, a)


if N == 1:
    answer = board[0][0]
else:
    solution(0, board)
print(answer)

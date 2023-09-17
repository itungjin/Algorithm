import sys

input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def horizontal_identity(r):
    for c in range(1, N):
        if board[r][c] != board[r][0]:
            return False
    return True


def vertical_identity(c):
    for r in range(1, N):
        if board[r][c] != board[0][c]:
            return False
    return True


def horizontal_ramp(r):
    used = [False] * N
    i = 1
    while i < N:
        if board[r][i] == board[r][i - 1]:
            i += 1
        else:
            if board[r][i] == board[r][i - 1] + 1:
                for j in range(i - L, i):
                    if j < 0:
                        return False
                    if used[j]:
                        return False
                    if board[r][j] == board[r][i - 1]:
                        used[j] = True
                    else:
                        return False
                i += 1
            elif board[r][i] == board[r][i - 1] - 1:
                for j in range(i, i + L):
                    if j >= N:
                        return False
                    if board[r][j] == board[r][i]:
                        used[j] = True
                    else:
                        return False
                i += L
            else:
                return False
    return True


def vertical_ramp(c):
    used = [False] * N
    i = 1
    while i < N:
        if board[i][c] == board[i - 1][c]:
            i += 1
        else:
            if board[i][c] == board[i - 1][c] + 1:
                for j in range(i - L, i):
                    if j < 0:
                        return False
                    if used[j]:
                        return False
                    if board[j][c] == board[i - 1][c]:
                        used[j] = True
                    else:
                        return False
                i += 1
            elif board[i][c] == board[i - 1][c] - 1:
                for j in range(i, i + L):
                    if j >= N:
                        return False
                    if board[j][c] == board[i][c]:
                        used[j] = True
                    else:
                        return False
                i += 1
            else:
                return False
    return True


for i in range(N):
    if horizontal_identity(i):
        answer += 1
    elif horizontal_ramp(i):
        answer += 1
    if vertical_identity(i):
        answer += 1
    elif vertical_ramp(i):
        answer += 1

print(answer)

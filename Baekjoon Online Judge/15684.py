import sys

input = sys.stdin.readline

N, M, H = map(int, input().split())
# N-1열은 반드시 모든 요소가 False
board = [[False] * N for _ in range(H)]
for _ in range(M):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = True
answer = 4


def start():
    for i in range(N):
        pos_r = 0
        pos_c = i
        while pos_r < H:
            if pos_c - 1 >= 0 and board[pos_r][pos_c - 1]:
                pos_c -= 1
            elif pos_c + 1 < N and board[pos_r][pos_c]:
                pos_c += 1
            pos_r += 1
        if pos_c != i:
            return False
    return True


def solution(n, r, c):
    global answer
    if n >= 4:
        return
    if start():
        answer = min(answer, n)
    for nc in range(c, N - 1):
        if not board[r][nc]:
            if (nc - 1 >= 0 and board[r][nc - 1]) or (nc + 1 < N - 1 and board[r][nc + 1]):
                continue
            board[r][nc] = True
            solution(n + 1, r, nc + 2)
            board[r][nc] = False
    for nr in range(r + 1, H):
        for nc in range(N - 1):
            if not board[nr][nc]:
                if (nc - 1 >= 0 and board[nr][nc - 1]) or (nc + 1 < N - 1 and board[nr][nc + 1]):
                    continue
                board[nr][nc] = True
                solution(n + 1, nr, nc)
                board[nr][nc] = False


solution(0, 0, 0)
if answer == 4:
    print(-1)
else:
    print(answer)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

nbr, nbc, nrr, nrc = 0, 0, 0, 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 'B':
            nbr, nbc = r, c
            board[r][c] = '.'
        elif board[r][c] == 'R':
            nrr, nrc = r, c
            board[r][c] = '.'

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

answer = 11
q = deque([(nbr, nbc, nrr, nrc, 1)])
while q:
    br, bc, rr, rc, t = q.popleft()
    for d in range(4):
        nbr, nbc, nrr, nrc = br, bc, rr, rc
        conflict_occur = False
        red_fall = False
        terminate = False

        while True:
            if nrr + dr[d] == nbr and nrc + dc[d] == nbc:
                if conflict_occur:
                    break
                conflict_occur = True
                while True:
                    if board[nbr + dr[d]][nbc + dc[d]] == '.':
                        nbr += dr[d]
                        nbc += dc[d]
                    elif board[nbr + dr[d]][nbc + dc[d]] == '#':
                        break
                    else:
                        terminate = True
                        break
            elif board[nrr + dr[d]][nrc + dc[d]] == '.':
                nrr += dr[d]
                nrc += dc[d]
            elif board[nrr + dr[d]][nrc + dc[d]] == '#':
                break
            else:
                red_fall = True
                nrr += dr[d]
                nrc += dc[d]
                break

        if terminate:
            continue

        # 파란 구슬 이동(빨간 구슬 이동시 파란 구슬을 이동하지 않았을 경우)
        if not conflict_occur:
            while True:
                if board[nbr + dr[d]][nbc + dc[d]] == 'O':
                    terminate = True
                    break
                elif nbr + dr[d] == nrr and nbc + dc[d] == nrc:
                    break
                elif board[nbr + dr[d]][nbc + dc[d]] == '.':
                    nbr += dr[d]
                    nbc += dc[d]
                else:
                    break
        if terminate:
            continue
        if red_fall:
            answer = t
        else:
            if t <= 9:
                q.append((nbr, nbc, nrr, nrc, t + 1))
    if answer != 11:
        break
if answer == 11:
    print(-1)
else:
    print(answer)

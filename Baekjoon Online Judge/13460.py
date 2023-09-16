import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

br, bc, rr, rc = 0, 0, 0, 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 'B':
            br, bc = r, c
            board[r][c] = '.'
        elif board[r][c] == 'R':
            rr, rc = r, c
            board[r][c] = '.'

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def tilt(d, br, bc, rr, rc):
    nbr, nbc, nrr, nrc = br, bc, rr, rc
    conflict_occur = False
    red_fall = False

    # 빨간 구슬 이동(필요시 파란 구슬 이동)
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
                    return False
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

    # 파란 구슬 이동(빨간 구슬 이동시 파란 구슬을 이동하지 않았을 경우)
    if not conflict_occur:
        while True:
            if board[nbr + dr[d]][nbc + dc[d]] == 'O':
                return False
            elif nbr + dr[d] == nrr and nbc + dc[d] == nrc:
                break
            elif board[nbr + dr[d]][nbc + dc[d]] == '.':
                nbr += dr[d]
                nbc += dc[d]
            else:
                break
    if red_fall:
        return True
    else:
        return nbr, nbc, nrr, nrc


answer = 11
case = int(pow(4, 10))
for t in range(case):
    temp = t
    pbr, pbc, prr, prc = br, bc, rr, rc
    for i in range(1, 11):
        ret = tilt(temp % 4, pbr, pbc, prr, prc)
        temp //= 4
        if ret == True:
            answer = min(answer, i)
            break
        elif ret == False:
            break
        else:
            pbr, pbc, prr, prc = ret
if answer == 11:
    print(-1)
else:
    print(answer)

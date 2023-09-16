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
    conflict_occur = False
    red_fall = False

    # 빨간 구슬 이동(필요시 파란 구슬 이동)
    while True:
        if rr + dr[d] == br and rc + dc[d] == bc:
            if conflict_occur:
                break
            conflict_occur = True
            while True:
                if board[br + dr[d]][bc + dc[d]] == '.':
                    br += dr[d]
                    bc += dc[d]
                elif board[br + dr[d]][bc + dc[d]] == '#':
                    break
                else:
                    return False
        elif board[rr + dr[d]][rc + dc[d]] == '.':
            rr += dr[d]
            rc += dc[d]
        elif board[rr + dr[d]][rc + dc[d]] == '#':
            break
        else:
            red_fall = True
            rr += dr[d]
            rc += dc[d]
            break

    # 파란 구슬 이동(빨간 구슬 이동시 파란 구슬을 이동하지 않았을 경우)
    if not conflict_occur:
        while True:
            if board[br + dr[d]][bc + dc[d]] == 'O':
                return False
            elif br + dr[d] == rr and bc + dc[d] == rc:
                break
            elif board[br + dr[d]][bc + dc[d]] == '.':
                br += dr[d]
                bc += dc[d]
            else:
                break
    if red_fall:
        return True
    else:
        return br, bc, rr, rc


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

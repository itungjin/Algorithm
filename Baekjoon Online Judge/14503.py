import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        answer += 1

    uncleaned_exist = False
    for i in range(1, 5):
        nd = (d - i) % 4
        nr, nc = r + dr[nd], c + dc[nd]
        if room[nr][nc] == 0:
            uncleaned_exist = True
            r, c = nr, nc
            d = nd
            break
    if uncleaned_exist:
        continue

    nr, nc = r - dr[d], c - dc[d]
    if room[nr][nc] != 1:
        r, c = nr, nc
    else:
        break

print(answer)

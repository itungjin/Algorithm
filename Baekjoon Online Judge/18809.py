from collections import deque
from copy import deepcopy

N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
answer = 0
available = [(r, c) for r in range(N) for c in range(M) if garden[r][c] == 2]
used = [False] * len(available)
cases_land = []


def get_case_land(n, i, temp_case):
    if n == G + R:
        cases_land.append(temp_case)
        return

    for j in range(i, len(available)):
        if not used[j]:
            used[j] = True
            get_case_land(n + 1, j + 1, temp_case + [[available[j][0], available[j][1]]])
            used[j] = False


get_case_land(0, 0, [])
case = [0] * G
cases = [[] for _ in range(len(cases_land))]


def get_cases(n, i, j):
    if n == G:
        cases[i].append(case[:])
        return

    for k in range(j, G + R):
        case[n] = k
        get_cases(n + 1, i, k + 1)


for i in range(len(cases_land)):
    get_cases(0, i, 0)

for i in range(len(cases)):
    for j in range(len(cases[i])):
        case = cases[i][j]
        g = deepcopy(garden)
        q = deque()
        temp = []
        for k in range(R + G):
            r, c = cases_land[i][k]
            if k in case:
                g[r][c] = 3
                q.append([r, c])
            else:
                g[r][c] = 4
                temp.append([r, c])
        for item in temp:
            q.append(item)

        time_line = [[0] * M for _ in range(N)]
        flower = set()

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        while q:
            r, c = q.popleft()
            if (r, c) in flower:
                continue

            if g[r][c] == 3:
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if g[nr][nc] == 1 or g[nr][nc] == 2:
                            g[nr][nc] = 3
                            time_line[nr][nc] = time_line[r][c] + 1
                            q.append([nr, nc])
            else:
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if g[nr][nc] == 1 or g[nr][nc] == 2:
                            g[nr][nc] = 4
                            time_line[nr][nc] = time_line[r][c] + 1
                            q.append([nr, nc])
                        elif g[nr][nc] == 3 and time_line[nr][nc] == time_line[r][c] + 1:
                            g[nr][nc] = -1
                            flower.add((nr, nc))
        answer = max(answer, len(flower))

print(answer)

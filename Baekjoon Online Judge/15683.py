from copy import deepcopy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1은 한쪽방향 (4가지 경우 가능)
# 왼 위 오른 아래
# 2는 양쪽방향 (2가지 경우 가능)
# 가로 세로
# 3는 직각 ( 4가지 경우 가능)
# 왼위, 위오른, 오른아래, 아래왼
# 4는 한 방향 빼고(4가지 경우 가능)
# 왼빼고, 위빼고, 오른빼고, 아래빼고
# 5는 4방향 (1가지 경우 가능)


cn = 0
ci = []
z = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cn += 1
            ci.append((i, j, arr[i][j]))
        if arr[i][j] == 0:
            z += 1
case = [0] * cn
answer = 64


def left(temp, r, c):
    count = 0
    for nc in range(c - 1, -1, -1):
        if temp[r][nc] == 6:
            break
        elif temp[r][nc] == 0:
            temp[r][nc] = -1
            count += 1

    return count


def right(temp, r, c):
    count = 0
    for nc in range(c + 1, M):
        if temp[r][nc] == 6:
            break
        elif temp[r][nc] == 0:
            temp[r][nc] = -1
            count += 1

    return count


def up(temp, r, c):
    count = 0
    for nr in range(r - 1, -1, -1):
        if temp[nr][c] == 6:
            break
        elif temp[nr][c] == 0:
            temp[nr][c] = -1
            count += 1

    return count


def down(temp, r, c):
    count = 0
    for nr in range(r + 1, N):
        if temp[nr][c] == 6:
            break
        elif temp[nr][c] == 0:
            temp[nr][c] = -1
            count += 1

    return count


def find_blind_spot():
    temp = deepcopy(arr)
    blind_spot = z
    for k in range(cn):
        r, c, num = ci[k]
        if num == 1:
            if case[k] == 0:
                blind_spot -= left(temp, r, c)
            elif case[k] == 1:
                blind_spot -= up(temp, r, c)
            elif case[k] == 2:
                blind_spot -= right(temp, r, c)
            elif case[k] == 3:
                blind_spot -= down(temp, r, c)
        elif num == 2:
            if case[k] == 0:
                blind_spot -= left(temp, r, c)
                blind_spot -= right(temp, r, c)
            elif case[k] == 1:
                blind_spot -= up(temp, r, c)
                blind_spot -= down(temp, r, c)
        elif num == 3:
            if case[k] == 0:
                blind_spot -= left(temp, r, c)
                blind_spot -= up(temp, r, c)
            elif case[k] == 1:
                blind_spot -= up(temp, r, c)
                blind_spot -= right(temp, r, c)
            elif case[k] == 2:
                blind_spot -= right(temp, r, c)
                blind_spot -= down(temp, r, c)
            elif case[k] == 3:
                blind_spot -= down(temp, r, c)
                blind_spot -= left(temp, r, c)
        elif num == 4:
            if case[k] == 0:
                blind_spot -= up(temp, r, c)
                blind_spot -= right(temp, r, c)
                blind_spot -= down(temp, r, c)
            elif case[k] == 1:
                blind_spot -= right(temp, r, c)
                blind_spot -= down(temp, r, c)
                blind_spot -= left(temp, r, c)
            elif case[k] == 2:
                blind_spot -= down(temp, r, c)
                blind_spot -= left(temp, r, c)
                blind_spot -= up(temp, r, c)
            elif case[k] == 3:
                blind_spot -= left(temp, r, c)
                blind_spot -= up(temp, r, c)
                blind_spot -= right(temp, r, c)
        elif num == 5:
            blind_spot -= left(temp, r, c)
            blind_spot -= up(temp, r, c)
            blind_spot -= right(temp, r, c)
            blind_spot -= down(temp, r, c)
    return blind_spot


def find_case(n):
    global answer

    if n == cn:
        answer = min(answer, find_blind_spot())
        return

    if ci[n][2] == 2:
        for i in range(2):
            case[n] = i
            find_case(n + 1)
    elif ci[n][2] == 5:
        find_case(n + 1)
    else:
        for i in range(4):
            case[n] = i
            find_case(n + 1)


find_case(0)
print(answer)

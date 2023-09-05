from collections import deque

arr = [list(input()) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
group = [[0, 0] for _ in range(7)]
count_s = 0
count_y = 0
answer = 0


def solution(n, r, c):
    global count_s
    global count_y

    if count_y > 3:
        return

    if n == 7:
        if count_s > count_y:
            if bfs():
                global answer
                answer += 1
        return

    for j in range(c + 1, 5):
        if not visited[r][j]:
            visited[r][j] = True
            if arr[r][j] == 'S':
                count_s += 1
            else:
                count_y += 1
            group[n] = [r, j]
            solution(n + 1, r, j)
            visited[r][j] = False
            if arr[r][j] == 'S':
                count_s -= 1
            else:
                count_y -= 1

    for i in range(r + 1, 5):
        for j in range(5):
            if not visited[i][j]:
                visited[i][j] = True
                if arr[i][j] == 'S':
                    count_s += 1
                else:
                    count_y += 1
                group[n] = [i, j]
                solution(n + 1, i, j)
                visited[i][j] = False
                if arr[i][j] == 'S':
                    count_s -= 1
                else:
                    count_y -= 1


def bfs():
    q = deque()
    q.append(group[0])
    v = [False] * 7
    v[0] = True

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            for j in range(7):
                if not v[j]:
                    if (nr, nc) == (group[j][0], group[j][1]):
                        q.append((nr, nc))
                        v[j] = True
    if all(v):
        return True
    else:
        return False


solution(0, 0, -1)
print(answer)

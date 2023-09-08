N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chickens = []
houses = []

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            houses.append((r, c))
        if arr[r][c] == 2:
            chickens.append((r, c))

chicken_distances = [[0] * len(chickens) for _ in range(len(houses))]
for i in range(len(houses)):
    for j in range(len(chickens)):
        chicken_distances[i][j] = (abs(houses[i][0] - chickens[j][0]) + abs(houses[i][1] - chickens[j][1]), j)
    chicken_distances[i].sort(key=lambda x: x[0])
close = [0] * (len(chickens) - M)
answer = 1e9


def solution(m, i):
    global answer
    if m == len(chickens) - M:
        temp_ans = 0
        c = set(close)
        for i in range(len(houses)):
            for j in range(len(chickens)):
                if chicken_distances[i][j][1] in c:
                    pass
                else:
                    temp_ans += chicken_distances[i][j][0]
                    break
        answer = min(answer, temp_ans)
        return

    for j in range(i, len(chickens)):
        close[m] = j
        solution(m + 1, j + 1)


solution(0, 0)
print(answer)

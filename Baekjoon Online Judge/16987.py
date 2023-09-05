N = int(input())
eggs = [list(map(int, input().split())) for i in range(N)]
answer = 0


def solution(n, broken):
    global answer
    answer = max(answer, broken)

    if n == N:
        return

    if eggs[n][0] <= 0:
        solution(n + 1, broken)
        return

    for i in range(N):
        if i == n or eggs[i][0] <= 0:
            continue

        eggs[n][0] -= eggs[i][1]
        eggs[i][0] -= eggs[n][1]

        if eggs[n][0] <= 0:
            if eggs[i][0] <= 0:
                solution(n + 1, broken + 2)
            else:
                solution(n + 1, broken + 1)
        else:
            if eggs[i][0] <= 0:
                solution(n + 1, broken + 1)
            else:
                solution(n + 1, broken)
        eggs[n][0] += eggs[i][1]
        eggs[i][0] += eggs[n][1]


solution(0, 0)
print(answer)

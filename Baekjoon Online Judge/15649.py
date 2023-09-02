N, M = map(int, input().split())

answer = [0] * M
used = [False] * (N + 1)


def recursion(a, n):
    answer[n] = a
    used[a] = True
    if n == M - 1:
        print(*answer)
    else:
        for j in range(1, N + 1):
            if not used[j]:
                recursion(j, n + 1)
    used[a] = False


for i in range(1, N + 1):
    recursion(i, 0)

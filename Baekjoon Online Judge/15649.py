N, M = map(int, input().split())

arr = [0] * M
is_used = [False] * (N + 1)


def solution(n):
    if n == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if not is_used[i]:
            arr[n] = i
            is_used[i] = True
            solution(n + 1)
            is_used[i] = False


solution(0)

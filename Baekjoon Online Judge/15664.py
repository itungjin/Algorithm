N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
is_used = [False] * N
answer = [0] * M


def solution(n, i):
    if n == M:
        print(*answer)
        return

    temp = -10001
    for j in range(i, N):
        if not is_used[j] and arr[j] != temp:
            is_used[j] = True
            answer[n] = arr[j]
            solution(n + 1, j + 1)
            is_used[j] = False
            temp = arr[j]


solution(0, 0)

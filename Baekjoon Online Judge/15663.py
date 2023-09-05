N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
is_used = [False] * N
answer = [0] * M


def solution(n):
    if n == M:
        print(*answer)
        return

    temp = -10001
    for i in range(N):
        if not is_used[i] and arr[i] != temp:
            answer[n] = arr[i]
            is_used[i] = True
            solution(n + 1)
            is_used[i] = False
            temp = arr[i]


solution(0)

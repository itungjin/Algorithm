N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
is_used = [False] * (N + 1)
answer = [0] * M


def solution(n):
    if n == M:
        print(*answer)
        return
    for i in range(1, N + 1):
        if not is_used[i]:
            is_used[i] = True
            answer[n] = arr[i - 1]
            solution(n + 1)
            is_used[i] = False


solution(0)

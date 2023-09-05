N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = [0] * M


def solution(n):
    if n == M:
        print(*answer)
        return

    temp = -10001
    for i in range(N):
        if arr[i] != temp:
            answer[n] = arr[i]
            solution(n + 1)
            temp = arr[i]


solution(0)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = [0] * M


def solution(n, i):
    if n == M:
        print(*answer)
        return

    temp = -10001
    for j in range(i, N):
        if arr[j] != temp:
            answer[n] = arr[j]
            solution(n + 1, j)
            temp = arr[j]


solution(0, 0)

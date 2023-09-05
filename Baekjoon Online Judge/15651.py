N, M = map(int, input().split())

arr = [0] * M


def solution(n):
    if n == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        arr[n] = i
        solution(n + 1)


solution(0)

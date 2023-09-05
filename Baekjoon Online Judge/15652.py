N, M = map(int, input().split())

arr = [0] * M


def solution(n, a):
    if n == M:
        print(*arr)
        return

    for i in range(a, N + 1):
        arr[n] = i
        solution(n + 1, i)


solution(0, 1)

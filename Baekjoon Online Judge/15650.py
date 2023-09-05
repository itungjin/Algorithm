N, M = map(int, input().split())

arr = [0] * M


def solution(n, l):
    arr[l] = n
    if l == M - 1:
        print(*arr)
        return

    for i in range(n + 1, N + 1):
        solution(i, l + 1)


for i in range(1, N + 1):
    solution(i, 0)

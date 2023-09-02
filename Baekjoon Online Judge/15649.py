N, M = map(int, input().split())

array = [0] * M
used = [False] * (N + 1)


def recursion(n):
    if n == M:
        print(*array)
        return
    for i in range(1, N + 1):
        if not used[i]:
            array[n] = i
            used[i] = True
            recursion(n + 1)
            used[i] = False


recursion(0)

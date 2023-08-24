N = int(input())

print(pow(2, N) - 1)


def hanoi(n, a, tmp, b):
    if n == 0:
        return
    hanoi(n - 1, a, b, tmp)
    print(a, b)
    hanoi(n - 1, tmp, a, b)


hanoi(N, 1, 2, 3)

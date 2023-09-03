N = int(input())

print(pow(2, N) - 1)


def solution(n, a, b, c):
    if n == 0:
        return

    solution(n - 1, a, c, b)
    print(a, c)
    solution(n - 1, b, a, c)


solution(N, 1, 2, 3)

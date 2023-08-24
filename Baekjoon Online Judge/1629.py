A, B, C = map(int, input().split())


def recursion(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 1:
        return recursion(a * a % c, b // 2, c) * a % c
    else:
        return recursion(a * a % c, b // 2, c)


print(recursion(A, B, C))

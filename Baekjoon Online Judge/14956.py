# k가 1일 때 1미터 걸음마다 90도 오른쪽 회전한다.
# k가 1보다 클 때, k - 1의 서브-패스웨이로 구성된다.

N, M = map(int, input().split())


# 2 3
# 1 4
def pat1(n, m, r, c):
    if n == 1:
        print(c + 1, N - r)
        return

    n //= 2
    area = n * n
    if m <= area:
        pat2(n, m, r, c)
    elif m <= 2 * area:
        pat1(n, m - area, r - n, c)
    elif m <= 3 * area:
        pat1(n, m - 2 * area, r - n, c + n)
    else:
        pat3(n, m - 3 * area, r - n + 1, c + 2 * n - 1)


# 4 3
# 1 2
def pat2(n, m, r, c):
    if n == 1:
        print(c + 1, N - r)
        return

    n //= 2
    area = n * n
    if m <= area:
        pat1(n, m, r, c)
    elif m <= 2 * area:
        pat2(n, m - area, r, c + n)
    elif m <= 3 * area:
        pat2(n, m - 2 * area, r - n, c + n)
    else:
        pat4(n, m - 3 * area, r - 2 * n + 1, c + n - 1)


# 2 1
# 3 4
def pat3(n, m, r, c):
    if n == 1:
        print(c + 1, N - r)
        return

    n //= 2
    area = n * n
    if m <= area:
        pat4(n, m, r, c)
    elif m <= 2 * area:
        pat3(n, m - area, r, c - n)
    elif m <= 3 * area:
        pat3(n, m - 2 * area, r + n, c - n)
    else:
        pat1(n, m - 3 * area, r + 2 * n - 1, c - n + 1)


# 4 1
# 3 2
def pat4(n, m, r, c):
    if n == 1:
        print(c + 1, N - r)
        return

    n //= 2
    area = n * n
    if m <= area:
        pat3(n, m, r, c)
    elif m <= 2 * area:
        pat4(n, m - area, r + n, c)
    elif m <= 3 * area:
        pat4(n, m - 2 * area, r + n, c - n)
    else:
        pat2(n, m - 3 * area, r + n - 1, c - 2 * n + 1)


pat1(N, M, N - 1, 0)

N, R, C = map(int, input().split())


def solution(n, r, c):
    if n == 0:
        return 0

    half = 1 << (n - 1)

    if R < r + n // 2 and C < c + n // 2:
        return solution(n // 2, r, c)
    elif R < r + n // 2 and c + n // 2 <= C:
        return half * half + solution(n // 2, r, c + n // 2)
    elif r + n // 2 <= R and C < c + n // 2:
        return 2 * half * half + solution(n // 2, r + n // 2, c)
    else:
        return 3 * half * half + solution(n // 2, r + n // 2, c + n // 2)


print(solution(N, 0, 0))

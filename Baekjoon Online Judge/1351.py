import sys

input = sys.stdin.readline

N, P, Q = map(int, input().split())
a = dict()


def solution(n):
    if n == 0:
        return 1
    if n not in a:
        a[n] = solution(n // P) + solution(n // Q)
    return a[n]


print(solution(N))

import sys

_input = sys.stdin.readline

N = int(input())
v = [list(map(int, _input().rstrip())) for _ in range(N)]


def is_identical(n, r, c):
    for i in range(n):
        for j in range(n):
            if v[r][c] != v[r + i][c + j]:
                return False
    return True


def solution(n, r, c):
    if is_identical(n, r, c):
        print(v[r][c], end='')
    else:
        print('(', end='')
        n //= 2
        for i in range(2):
            for j in range(2):
                solution(n, r + i * n, c + j * n)
        print(')', end='')


solution(N, 0, 0)

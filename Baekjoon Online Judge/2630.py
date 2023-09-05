import sys

_input = sys.stdin.readline

N = int(input())
cp = [list(map(int, _input().split())) for _ in range(N)]
answer = [0, 0]


def is_identical(n, r, c):
    for i in range(n):
        for j in range(n):
            if cp[r][c] != cp[r + i][c + j]:
                return False
    return True


def solution(n, r, c):
    if is_identical(n, r, c):
        answer[cp[r][c]] += 1
    else:
        n //= 2
        for i in range(2):
            for j in range(2):
                solution(n, r + i * n, c + j * n)


solution(N, 0, 0)
print(answer[0])
print(answer[1])

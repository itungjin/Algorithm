import sys

_input = sys.stdin.readline

N = int(input())
paper = [list(map(int, _input().split())) for _ in range(N)]
answer = [0, 0, 0]


def is_identical(n, r, c):
    for i in range(n):
        for j in range(n):
            if paper[r][c] != paper[r + i][c + j]:
                return False
    return True


def solution(n, r, c):
    if is_identical(n, r, c):
        answer[paper[r][c] + 1] += 1
    else:
        n //= 3
        for i in range(3):
            for j in range(3):
                solution(n, r + i * n, c + j * n)


solution(N, 0, 0)
print(answer[0])
print(answer[1])
print(answer[2])

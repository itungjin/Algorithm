import sys

input = sys.stdin.readline

N = int(input().rstrip())
papers = [list(map(int, input().split())) for _ in range(N)]
color = [0] * 2


def cut_check(n, r, c):
    for i in range(r, r + n):
        for j in range(c, c + n):
            if papers[r][c] != papers[i][j]:
                return True
    return False


def search(n, r, c):
    if not cut_check(n, r, c):
        color[papers[r][c]] += 1
        return
    n = n // 2
    nr = [0, 0, n, n]
    nc = [0, n, 0, n]
    for i in range(4):
        search(n, r + nr[i], c + nc[i])


search(N, 0, 0)
print(color[0])
print(color[1])

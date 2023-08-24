import sys

input = sys.stdin.readline

N = int(input().rstrip())
paper = [list(map(int, input().split())) for _ in range(N)]

count = [0] * 3


def search(n, r, c):
    same = True
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[r][c] != paper[i][j]:
                same = False
                break
        if not same:
            break
    if same:
        count[paper[r][c] + 1] += 1
    else:
        n //= 3
        for i in range(3):
            for j in range(3):
                search(n, r + i * n, c + j * n)


search(N, 0, 0)
for i in range(3):
    print(count[i])

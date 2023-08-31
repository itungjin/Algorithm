N = int(input())
stars = [[' '] * (2 * N - 1) for _ in range(N)]


def recursion(n, r, c):
    if n == 3:
        stars[r][c] = '*'
        stars[r + 1][c - 1] = stars[r + 1][c + 1] = '*'
        for i in range(3):
            stars[r + 2][c - i] = '*'
            stars[r + 2][c + i] = '*'
    else:
        n //= 2
        recursion(n, r, c)
        recursion(n, r + n, c - n)
        recursion(n, r + n, c + n)


recursion(N, 0, N - 1)
for i in range(len(stars)):
    for j in range(len(stars[i])):
        print(stars[i][j], end='')
    print()

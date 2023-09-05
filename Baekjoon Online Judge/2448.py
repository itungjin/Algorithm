N = int(input())
arr = [[' '] * (2 * N - 1) for _ in range(N)]


def star(n, r, c):
    if n == 3:
        arr[r][c] = '*'
        arr[r + 1][c - 1] = '*'
        arr[r + 1][c + 1] = '*'
        for i in range(-2, 3):
            arr[r + 2][c + i] = '*'
    else:
        n //= 2
        star(n, r, c)
        star(n, r + n, c - n)
        star(n, r + n, c + n)


star(N, 0, N - 1)
for i in range(N):
    for char in arr[i]:
        print(char, end='')
    print()
N = int(input())
arr = [[' '] * (2 * N - 1) for _ in range(N)]


def star(n, r, c):
    if n == 3:
        arr[r][c] = '*'
        arr[r + 1][c - 1] = '*'
        arr[r + 1][c + 1] = '*'
        for i in range(-2, 3):
            arr[r + 2][c + i] = '*'
    else:
        n //= 2
        star(n, r, c)
        star(n, r + n, c - n)
        star(n, r + n, c + n)


star(N, 0, N - 1)
for i in range(N):
    for char in arr[i]:
        print(char, end='')
    print()

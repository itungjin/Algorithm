N = int(input())
stars = [[' '] * N for _ in range(N)]


def recursion(n, a, b):
    if n >= 3:
        n //= 3
        da = [0, 0, 0, n, n, 2 * n, 2 * n, 2 * n]
        db = [0, n, 2 * n, 0, 2 * n, 0, n, 2 * n]
        for i in range(8):
            recursion(n, a + da[i], b + db[i])
    else:
        stars[a][b] = '*'


recursion(N, 0, 0)
for star in stars:
    for s in star:
        print(s, end='')
    print()

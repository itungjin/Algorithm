N = int(input())

square = [[' '] * N for _ in range(N)]


def solution(n, r, c):
    if n == 1:
        square[r][c] = '*'
    else:
        n //= 3
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):
                    solution(n, r + i * n, c + j * n)


solution(N, 0, 0)
for i in range(N):
    for j in range(N):
        print(square[i][j], end='')
    print()

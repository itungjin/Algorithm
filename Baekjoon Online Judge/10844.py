N = int(input())
d = [[0] * 10 for _ in range(N)]
d[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, N):
    d[i][0] = d[i - 1][1]
    for j in range(1, 9):
        d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]
    d[i][9] = d[i - 1][8]
print(sum(d[N - 1]) % 1000000000)

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]
count = dict()
strings = [""] * K
for i in range(K):
    string = input().rstrip()
    count[string] = 0
    strings[i] = string
strings_set = set(strings)
move = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
dp = [[[[] for _ in range(5)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        dp[i][j][0].append(grid[i][j])
        if grid[i][j] in strings_set:
            count[grid[i][j]] += 1
for n in range(4):
    for i in range(N):
        for j in range(M):
            for s in dp[i][j][n]:
                for di, dj in move:
                    ni, nj = (i + di) % N, (j + dj) % M
                    ns = s + grid[ni][nj]
                    dp[ni][nj][n + 1].append(ns)
                    if ns in strings_set:
                        count[ns] += 1

for string in strings:
    print(count[string])

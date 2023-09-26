import sys

D = 1000000

input = sys.stdin.readline
password = list(map(int, input().rstrip()))
n = len(password)
dp = [[0, 0] for _ in range(n + 1)]
if password[0] == 0:
    print(0)
    exit(0)
dp[0][0] = 1
dp[1][0] = 1
for i in range(2, n + 1):
    if password[i - 2] == 1:
        dp[i][1] = (dp[i - 2][0] + dp[i - 2][1]) % D
    elif password[i - 2] == 2 and password[i - 1] <= 6:
        dp[i][1] = (dp[i - 2][0] + dp[i - 2][1]) % D
    if password[i - 1] == 0:
        dp[i][0] = 0
    else:
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % D
    if dp[i][0] == 0 and dp[i][1] == 0:
        print(0)
        exit(0)
print((dp[n][0] + dp[n][1]) % D)

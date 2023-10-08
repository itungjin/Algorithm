import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
for i in range(0, len(s2)):
    if s1[0] == s2[i]:
        for j in range(i, len(s2)):
            dp[0][j] = 1
        break
for i in range(0, len(s1)):
    if s1[i] == s2[0]:
        for j in range(i, len(s1)):
            dp[j][0] = 1
        break

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1], dp[i - 1][j])
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
print(dp[len(s1) - 1][len(s2) - 1])

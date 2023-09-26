import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
n1 = len(s1)
n2 = len(s2)
dp = [[0 for _ in range(n2)] for _ in range(n1)]
answer = 0
mapping = [[] for _ in range(n1)]
for i in range(n1):
    if s1[i] == s2[0]:
        answer = 1
        dp[i][0] = 1
    for j in range(1, n2):
        if s1[i] == s2[j]:
            mapping[i].append(j)
            answer = 1
            dp[i][j] = 1
        elif dp[i][j - 1] == 1:
            dp[i][j] = 1
for i in range(1, n1):
    temp = dp[i - 1][0]
    if dp[i][0] < temp:
        dp[i][0] = temp
    for j in range(1, n2):
        if s1[i] == s2[j]:
            if max(dp[i - 1][j - 1] + 1, dp[i - 1][j]) > temp:
                temp = max(dp[i - 1][j - 1] + 1, dp[i - 1][j])
        else:
            if dp[i - 1][j] > temp:
                temp = dp[i - 1][j]
        if dp[i][j] < temp:
            dp[i][j] = temp
answer = max(answer, dp[n1 - 1][n2 - 1])
print(answer)

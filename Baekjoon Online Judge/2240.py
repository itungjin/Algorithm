import sys

input = sys.stdin.readline

T, W = map(int, input().split())
p = [int(input().rstrip()) for _ in range(T)]
count_first = [0] * T
count_second = [0] * T
if p[0] == 1:
    count_first[0] = 1
else:
    count_second[0] = 1
for i in range(1, T):
    count_first[i] = count_first[i - 1]
    count_second[i] = count_second[i - 1]
    if p[i] == 1:
        count_first[i] += 1
    else:
        count_second[i] += 1

dp = [[0] * (W + 1) for _ in range(T)]
dp[0][0] = count_first[T - 1]
dp[0][1] = count_second[T - 1]
answer = max(dp[0][0], dp[0][1])
for i in range(1, T):
    dp[i][0] = count_first[T - 1]
    for k in range(i):
        for j in range(1, W + 1):
            if j - 2 > k:
                break
            if j % 2 == 0:
                dp[i][j] = max(dp[i][j], dp[k][j - 1] - (count_second[T - 1] - count_second[i]) + (
                        count_first[T - 1] - count_first[i]))
            else:
                dp[i][j] = max(dp[i][j], dp[k][j - 1] + (count_second[T - 1] - count_second[i]) - (
                        count_first[T - 1] - count_first[i]))
    answer = max(answer, max(dp[i]))
print(answer)

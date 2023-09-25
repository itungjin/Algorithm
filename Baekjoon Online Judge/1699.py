INF = int(1e9)
N = int(input())

dp = [INF] * (N + 1)
dp[0] = 0
square_numbers = []
n = 0
for i in range(1, N + 1):
    if i == (n + 1) ** 2:
        n += 1
        dp[i] = 1
        square_numbers.append(n ** 2)
    else:
        for square_number in square_numbers:
            dp[i] = min(dp[i], dp[i - square_number] + 1)
print(dp[N])

N = int(input())
if N == 1:
    print(1)
    exit(0)
dp = [0 for _ in range(N)]
dp[0] = 1  # 1
dp[1] = 2  # 00, 11
for i in range(2, N):
    # 00으로 끝나는 경우: dp[i - 2]의 수열 뒤에 00을 추가
    # 1으로 끝나는 경우: dp[i - 1]의 수열 뒤에 1을 추가
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
print(dp[N - 1] % 15746)

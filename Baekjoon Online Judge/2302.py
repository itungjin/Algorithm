import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
vip = set(int(input().rstrip()) for _ in range(M))
dp = [[0, 0, 0] for _ in range(N + 1)]
if N == 1:
    print(1)
    exit(0)
if 1 not in vip:
    dp[1][2] = 1
dp[1][1] = 1
if 2 not in vip:
    dp[2][0] = dp[1][2]
    dp[2][2] = dp[1][1]
dp[2][1] = dp[1][1]
for i in range(2, N + 1):
    if i not in vip:
        # 내가 앞 좌석에 앉으려면 앞좌석 사람이 내 자리에 앉아야함
        dp[i][0] = dp[i - 1][2]
        # 내가 뒷 좌석에 앉을려면 앞 좌석 사람은 앞앞좌석이나 앞좌석에 앉아야함
        dp[i][2] = dp[i - 1][0] + dp[i - 1][1]
    # 내가 내 자리에 앉으려면 앞 좌석 사람이 앞앞좌석이나 앞좌석에 앉아야함
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1]
print(dp[N][0] + dp[N][1])

import sys

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    stocks = list(map(int, input().split()))
    max_index = [0] * N
    max_index[N - 1] = N - 1
    for i in range(N - 2, -1, -1):
        if stocks[max_index[i + 1]] <= stocks[i]:
            max_index[i] = i
        else:
            max_index[i] = max_index[i + 1]
    now = 0
    answer = 0
    while now < N - 1:
        sell = max_index[now]
        if now == sell:
            now += 1
            continue
        answer += stocks[sell] * (sell - now) - sum(stocks[now:sell])
        now = sell + 1
    print(answer)

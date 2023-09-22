import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))

dp = [1] * N

max_length_index = 0
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    if dp[i] > dp[max_length_index]:
        max_length_index = i

max_length = dp[max_length_index]
print(max_length)
max_length_sequence = [A[max_length_index]]
for i in range(max_length_index - 1, -1, -1):
    if dp[i] == max_length - 1 and A[i] < max_length_sequence[-1]:
        max_length_sequence.append(A[i])
        max_length -= 1
for i in range(len(max_length_sequence) - 1, -1, -1):
    print(max_length_sequence[i], end=' ')

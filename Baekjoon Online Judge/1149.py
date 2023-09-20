import sys

input = sys.stdin.readline

N = int(input().rstrip())
answers = [[0] * 3 for _ in range(N)]
costs = [list(map(int, input().split())) for _ in range(N)]

for i in range(3):
    answers[0][i] = costs[0][i]
for i in range(1, N):
    for j in range(3):
        answers[i][j] = min(answers[i - 1][(j - 1) % 3], answers[i - 1][(j + 1) % 3]) + costs[i][j]
print(min(answers[N - 1]))

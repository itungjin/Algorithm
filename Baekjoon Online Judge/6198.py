import sys

input = sys.stdin.readline

N = int(input().rstrip())
h = [int(input().rstrip()) for _ in range(N)]

answer = 0
stack = []
for i in range(0, N):
    while stack and h[i] >= stack[-1][0]:
        answer += i - stack.pop()[1] - 1
    stack.append((h[i], i))
while stack:
    answer += N - stack.pop()[1] - 1
print(answer)

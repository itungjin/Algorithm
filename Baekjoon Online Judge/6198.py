import sys

input = sys.stdin.readline

h = [0] * 80000
N = int(input().rstrip())
for i in range(N):
    h[i] = int(input().rstrip())
stack = []
answer = 0
for i in range(N):
    while stack and h[stack[-1]] <= h[i]:
        answer += i - stack[-1] - 1
        stack.pop()
    stack.append(i)
stack.pop()
while stack:
    answer += N - stack[-1] - 1
    stack.pop()
print(answer)

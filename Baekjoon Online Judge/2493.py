import sys

input = sys.stdin.readline

N = int(input().rstrip())
towers = list(map(int, input().split()))

answer = [0] * N
stack = [(towers[0], 1)]
for i in range(1, N):
    while stack and towers[i] > stack[-1][0]:
        stack.pop()
    if stack:
        answer[i] = stack[-1][1]
    stack.append((towers[i], i + 1))
print(*answer)

import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
stack = []
answer = [0] * N
for i in range(N - 1, -1, -1):
    while stack and stack[-1] <= A[i]:
        stack.pop()
    if not stack:
        answer[i] = -1
    else:
        answer[i] = stack[-1]
    stack.append(A[i])
print(*answer)

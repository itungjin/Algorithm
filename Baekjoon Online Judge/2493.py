import sys

input = sys.stdin.readline

N = int(input().rstrip())
towers = list(map(int, input().split()))
stack = []
for i in range(N):
    while stack and towers[stack[-1]] < towers[i]:
        stack.pop()
    if not stack:
        print(0, end=' ')
    else:
        print(stack[-1] + 1, end=' ')
    stack.append(i)

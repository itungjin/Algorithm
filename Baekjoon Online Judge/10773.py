import sys

input = sys.stdin.readline

stack = [0] * 100000
top = 0

K = int(input().rstrip())
for _ in range(K):
    num = int(input().rstrip())
    if num == 0:
        top -= 1
    else:
        stack[top] = num
        top += 1
ans = 0
for i in range(0, top):
    ans += stack[i]
print(ans)

import sys

input = sys.stdin.readline

N = int(input().rstrip())
s = [int(input().rstrip()) for _ in range(N)]
answer = 0
for i in range(N - 2, -1, -1):
    if s[i] >= s[i + 1]:
        answer += s[i] - s[i + 1] + 1
        s[i] = s[i + 1] - 1
print(answer)

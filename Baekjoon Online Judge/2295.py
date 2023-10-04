import sys

input = sys.stdin.readline

N = int(input().rstrip())
U = [int(input().rstrip()) for _ in range(N)]
U.sort()
u2 = set()
for i in range(N):
    for j in range(N):
        u2.add(U[i] + U[j])
answer = 0
for i in range(N):
    for j in range(i + 1, N):
        if U[j] - U[i] in u2:
            answer = max(answer, U[j])
print(answer)

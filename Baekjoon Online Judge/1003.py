import sys

input = sys.stdin.readline

fibonacci = [0] * 41
fibonacci[0] = (1, 0)
fibonacci[1] = (0, 1)
for i in range(2, 41):
    fibonacci[i] = (fibonacci[i - 1][0] + fibonacci[i - 2][0], fibonacci[i - 1][1] + fibonacci[i - 2][1])
T = int(input().rstrip())
for _ in range(T):
    print(*fibonacci[int(input().rstrip())])

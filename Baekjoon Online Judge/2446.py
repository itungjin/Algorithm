# 구현

N = int(input())

for i in range(1, N+1):
    print(' ' * (i-1) + '*' * (2 * (N-i) + 1))
for i in range(N-1, 0, -1):
    print(' ' * (i-1) + '*' * (2 * (N-i) + 1))

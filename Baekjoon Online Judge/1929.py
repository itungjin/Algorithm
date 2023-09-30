import math

M, N = map(int, input().split())
is_prime = [True] * (N + 1)
is_prime[1] = False
for i in range(2, int(math.sqrt(N+1)) + 1):
    if is_prime[i]:
        for j in range(i, N+1):
            if i*j >= N+1:
                break
            is_prime[i*j] = False
for i in range(M, N+1):
    if is_prime[i]:
        print(i)
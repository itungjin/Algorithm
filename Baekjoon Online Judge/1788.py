D = int(1e9)
N = 1000000
f = [0] * (N + 1)
f[0] = 0
f[1] = 1
for i in range(2, N + 1):
    f[i] = (f[i - 1] + f[i - 2]) % D
n = int(input())
if n == 0:
    print(0)
    print(0)
elif n < 0:
    if n % 2 == 0:
        print(-1)
    else:
        print(1)
    print(f[abs(n)])
else:
    print(1)
    print(f[n])

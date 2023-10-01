N, K = map(int, input().split())
top = 1
bottom = 1
for i in range(K):
    top *= (N - i)
for i in range(K, 0, -1):
    bottom *= i
print(top // bottom)

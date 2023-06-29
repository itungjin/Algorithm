# 구현

N = int(input())

# 0번째 줄부터 N-1번째 줄까지는 공백이 N-1-i개 *은 2i+1개
# N-1번째 줄을 기준으로 대칭

for i in range(N):
    print(" " * (N-1-i) + "*" * (2*i+1))
for i in range(N - 2, -1, -1):
    print(" " * (N-1-i) + "*" * (2*i+1))

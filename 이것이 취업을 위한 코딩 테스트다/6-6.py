# 정렬

N = int(input())
data = []
for _ in range(N):
    name, score = input().split()
    data.append([name, int(score)])
data.sort(key=lambda x: x[1])

for i in range(N):
    print(data[i][0], end=' ')

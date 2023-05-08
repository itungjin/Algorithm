# 그리디
# N은 볼링공의 개수 M은 볼링공의 최대 무게
# 무게별로 볼링공의 개수를 세어 배열에 저장

n, m = map(int, input().split())
k = list(map(int, input().split()))
answer = 0

balls = [0] * (m + 1)
for weight in k:
    balls[weight] += 1


for i in range(n):
    answer += n - balls[k[i]]

print(answer // 2)

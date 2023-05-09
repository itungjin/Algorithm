# 구현
# 완전 탐색
# n은 시간 범위
# 00시 00분 00초에서 n시 59분 59초까지 3을 포함하는 시각

n = int(input())
answer = 0

for i in range(0, n + 1):
    for j in range(0, 60):
        for k in range(0, 60):
            if '3' in f'{i}{j}{k}':
                answer += 1

print(answer)
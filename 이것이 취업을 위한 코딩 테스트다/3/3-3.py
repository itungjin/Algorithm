# 그리디
# n은 행의 개수, m은 열의 개수
# 행을 선택할 때 행의 가장 숫자가 낮은 카드 중 그 숫자가 가장 큰 행을 선택한다

n, m = map(int, input().split())
answer = 0
for i in range(n):
    answer = max(answer, min(list(map(int, input().split()))))

print(answer)

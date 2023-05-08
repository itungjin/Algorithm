# 그리디
# 배열의 크기는 N
# 더하는 횟수 M
# 배열의 요소를 연속으로 최대 K번 더할 수 있음
# K+1마다의 주기성을 이용

n, m, k = map(int, input().split())
array = list(map(int, input().split()))
answer = 0

array.sort(reverse=True)
answer = (array[0] * k + array[1]) * (m // (k + 1)) + array[0] * (m % (k + 1))

print(answer)

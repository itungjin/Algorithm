# 구현
# 현재 캐릭터의 점수 N(자릿수는 항상 짝수)

n = input()

left = n[0:len(n) // 2]
right = n[len(n) // 2: len(n)]
left_sum = 0
right_sum = 0

for i in range(len(left)):
    left_sum += int(left[i])

for i in range(len(right)):
    right_sum += int(right[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

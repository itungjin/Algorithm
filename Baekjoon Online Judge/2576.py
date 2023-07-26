# 구현

sum_odd = 0
min_odd = 100

for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        min_odd = min(min_odd, num)
        sum_odd += num

if sum_odd == 0:
    print(-1)
else:
    print(sum_odd)
    print(min_odd)

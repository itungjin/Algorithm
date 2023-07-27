# 구현

A = int(input())
B = int(input())
C = int(input())

digits = [0] * 10
result = str(A * B * C)
for digit in result:
    digits[int(digit)] += 1

for digit in digits:
    print(digit)

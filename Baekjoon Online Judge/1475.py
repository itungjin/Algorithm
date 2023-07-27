# 구현

N = input()

digits = [0] * 10

for digit in N:
    digits[int(digit)] += 1

max_val = (digits[6] + digits[9] + 1) // 2
digits[6], digits[9] = 0, 0
for digit in digits:
    max_val = max(max_val, digit)

print(max_val)

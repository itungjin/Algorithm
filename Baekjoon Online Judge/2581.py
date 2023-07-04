# 구현

import math

M = int(input())
N = int(input())


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


first_prime_num = 0
total_sum = 0
for i in range(M, N+1):
    if is_prime(i):
        if first_prime_num == 0:
            first_prime_num = i
        total_sum += i

if first_prime_num == 0:
    print(-1)
else:
    print(total_sum)
    print(first_prime_num)

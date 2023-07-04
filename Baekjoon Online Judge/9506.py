# 구현

import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == -1:
        break

    total_sum = 0
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            total_sum += i
            divisors.append(i)

    if total_sum == n:
        print(f'{n} = {divisors[0]}', end='')
        for i in range(1, len(divisors)):
            print(f' + {divisors[i]}', end='')
        print()
    else:
        print(f'{n} is NOT perfect.')

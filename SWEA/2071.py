# 구현

import math

T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))

    print(f'#{test_case} {int((sum(numbers) / 10) + 0.5)}')

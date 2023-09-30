import math
import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().split()))
answer = 0
for num in nums:
    if num == 1:
        continue
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        answer += 1
print(answer)

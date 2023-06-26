# 구현, 수학

number_of_divisors = int(input())
divisors = list(map(int, input().split()))

divisors.sort()
N = divisors[0] * divisors[number_of_divisors - 1]

print(N)

# 구현

N = int(input())
numbers = list(map(int, input().split()))


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


answer = 0
for number in numbers:
    if is_prime(number):
        answer += 1

print(answer)

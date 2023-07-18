# 구현

T = int(input())

for test_case in range(1, T+1):
    numbers = [number for number in list(
        map(int, input().split())) if number % 2 == 1]

    print(f"#{test_case} {sum(numbers)}")

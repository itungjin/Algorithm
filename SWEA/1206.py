# 구현

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))

    answer = 0
    for i in range(2, n - 2):
        for j in range(1, data[i] + 1):
            if data[i - 2] < j and data[i - 1] < j and data[i + 1] < j and data[i + 2] < j:
                answer += 1

    print(f"#{test_case} {answer}")

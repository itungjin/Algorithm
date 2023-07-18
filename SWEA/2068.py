# 구현

T = int(input())

for test_case in range(1, T + 1):
    print('#' + str(test_case), end=' ')

    nums = list(map(int, input().split()))
    print(max(nums))

# 구현

T = int(input())

for test_case in range(1, T + 1):
    num1, num2 = map(int, input().split())

    print('#' + str(test_case), end=' ')
    if num1 == num2:
        print('=')
    elif num1 > num2:
        print('>')
    else:
        print('<')

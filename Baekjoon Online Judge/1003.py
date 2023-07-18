# 구현
# 다이나믹 프로그래밍

T = int(input())

fibonacci = [(1, 0), (0, 1)]

for n in range(2, 41):
    fibonacci.append(
        (fibonacci[n-2][0] + fibonacci[n-1][0], fibonacci[n-2][1] + fibonacci[n-1][1]))

for _ in range(T):
    n = int(input())

    print(fibonacci[n][0], fibonacci[n][1])

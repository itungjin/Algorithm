N = 4
gear = [list(map(int, input())) for _ in range(N)]
K = int(input())


def clock(n, before):
    if before == -1:
        if n + 1 < N and gear[n][2] != gear[n + 1][6]:
            reverse_clock(n + 1, n)
        if n - 1 >= 0 and gear[n - 1][2] != gear[n][6]:
            reverse_clock(n - 1, n)
    else:
        if n > before:
            if n + 1 < N and gear[n][2] != gear[n + 1][6]:
                reverse_clock(n + 1, n)
        else:
            if n - 1 >= 0 and gear[n - 1][2] != gear[n][6]:
                reverse_clock(n - 1, n)
    gear[n] = gear[n][-1:] + gear[n][:-1]


def reverse_clock(n, before):
    if before == -1:
        if n + 1 < N and gear[n][2] != gear[n + 1][6]:
            clock(n + 1, n)
        if n - 1 >= 0 and gear[n - 1][2] != gear[n][6]:
            clock(n - 1, n)
    else:
        if n > before:
            if n + 1 < N and gear[n][2] != gear[n + 1][6]:
                clock(n + 1, n)
        else:
            if n - 1 >= 0 and gear[n - 1][2] != gear[n][6]:
                clock(n - 1, n)
    gear[n] = gear[n][1:] + gear[n][0:1]


for _ in range(K):
    a, b = map(int, input().split())
    if b == 1:
        clock(a - 1, -1)
    else:
        reverse_clock(a - 1, -1)

answer = 0
for i in range(N):
    if gear[i][0] == 1:
        answer += 2 ** i
print(answer)

import sys

input = sys.stdin.readline
answer = [0] * 6


def solution(n, i):
    if n == 6:
        print(*answer)
        return

    for j in range(i, k):
        answer[n] = S[j]
        solution(n + 1, j + 1)


while True:
    tc = list(map(int, input().split()))
    if len(tc) == 1 and tc[0] == 0:
        break

    k, S = tc[0], tc[1:]
    solution(0, 0)
    print()

import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
if S == 0:
    answer = -1


def solution(n, _sum):
    if n == N:
        if _sum == S:
            global answer
            answer += 1
        return

    solution(n + 1, _sum + arr[n])
    solution(n + 1, _sum)


solution(0, 0)
print(answer)

import sys

input = sys.stdin.readline

N = int(input().rstrip())
stairs = [int(input().rstrip()) for _ in range(N)]


def solution():
    if N <= 2:
        answer = 0
        for i in range(N):
            answer += stairs[i]
        print(answer)
        return

    answers = [0] * N
    answers[0] = stairs[0]
    answers[1] = stairs[0] + stairs[1]
    answers[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, N):
        answers[i] = max(answers[i - 3] + stairs[i - 1] + stairs[i], answers[i - 2] + stairs[i])
    print(answers[N - 1])


solution()

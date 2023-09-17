import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))
used_opr = [0] * 4
opr_seq = [0] * (N - 1)
answer_max = -int(1e9)
answer_min = int(1e9)


def calculate():
    global answer_max, answer_min
    result = A[0]
    for i in range(N - 1):
        if opr_seq[i] == 0:
            result += A[i + 1]
        elif opr_seq[i] == 1:
            result -= A[i + 1]
        elif opr_seq[i] == 2:
            result *= A[i + 1]
        else:
            if result < 0 < A[i + 1]:
                result = -result
                result //= A[i + 1]
                result = -result
            else:
                result //= A[i + 1]
    answer_max = max(answer_max, result)
    answer_min = min(answer_min, result)


def solution(n):
    if n == N - 1:
        calculate()
        return
    for i in range(4):
        if operators[i] > used_opr[i]:
            used_opr[i] += 1
            opr_seq[n] = i
            solution(n + 1)
            used_opr[i] -= 1


solution(0)
print(answer_max)
print(answer_min)

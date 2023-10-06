import sys

input = sys.stdin.readline

N, M = map(int, input().split())
by_num = [0] * (N + 1)
by_name = dict()
for i in range(1, N + 1):
    name = input().rstrip()
    by_num[i] = name
    by_name[name] = i
for i in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(by_num[int(question)])
    else:
        print(by_name[question])

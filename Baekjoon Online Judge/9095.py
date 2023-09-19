import sys

input = sys.stdin.readline

answers = [0] * 11
answers[1] = 1
answers[2] = 2
answers[3] = 4
for i in range(4, 11):
    answers[i] = answers[i - 1] + answers[i - 2] + answers[i - 3]

T = int(input().rstrip())

for _ in range(T):
    print(answers[int(input().rstrip())])

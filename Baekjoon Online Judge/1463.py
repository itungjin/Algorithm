X = int(input())

answers = [0] * (X + 1)


def solution(x):
    if x == 1:
        return 0
    if solution(x) != 0:
        return answers[x]
    answers[x] = min(answers[x], solution(x - 1) + 1)
    if x % 3 == 0:
        answers[x] = min(answers[x], solution(x // 3) + 1)
    if x % 2 == 0:
        answers[x] = min(answers[x], solution(x // 2) + 1)
    return answers[x]


for i in range(2, X + 1):
    answers[i] = answers[i - 1] + 1
    if i % 3 == 0:
        answers[i] = min(answers[i], answers[i // 3] + 1)
    if i % 2 == 0:
        answers[i] = min(answers[i], answers[i // 2] + 1)
print(answers[-1])

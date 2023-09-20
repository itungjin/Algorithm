X = int(input())

if X == 1:
    print(0)
    print(1)
    exit(0)
elif X <= 3:
    print(1)
    print(X, 1)
    exit(0)

answers = [0] * (X + 1)

answers[2] = 1
answers[3] = 1
for i in range(4, X + 1):
    answers[i] = answers[i - 1] + 1
    if i % 3 == 0:
        answers[i] = min(answers[i], answers[i // 3] + 1)
    if i % 2 == 0:
        answers[i] = min(answers[i], answers[i // 2] + 1)
print(answers[X])
while X > 1:
    print(X, end=' ')
    if answers[X] == answers[X - 1] + 1:
        X -= 1
    elif X % 3 == 0 and answers[X] == answers[X // 3] + 1:
        X //= 3
    else:
        X //= 2
print(1)

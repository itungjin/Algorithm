n = int(input())

if n == 1:
    print(1)
else:
    answers = [0] * n
    answers[0] = 1
    answers[1] = 2
    for i in range(2, n):
        answers[i] = (answers[i - 1] + answers[i - 2]) % 10007
    print(answers[n - 1])

N = int(input())
answers = [0 for _ in range(N + 1)]
answers[1] = (0, 1)
for i in range(2, N + 1):
    answers[i] = (answers[i - 1][0] + answers[i - 1][1], answers[i - 1][0])
print(answers[N][0] + answers[N][1])

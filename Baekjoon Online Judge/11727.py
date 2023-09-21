n = int(input())
if n == 1:
    print(1)
    exit(0)
answers = [0] * n
answers[0] = 1
answers[1] = 3
for i in range(2, n):
    answers[i] = (answers[i - 2] * 2 + answers[i - 1]) % 10007
print(answers[n - 1])

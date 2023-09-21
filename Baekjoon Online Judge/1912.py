import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))
answers = [0] * n
answers[0] = nums[0]
answer = answers[0]
for i in range(1, n):
    answers[i] = max(answers[i - 1] + nums[i], nums[i])
    answer = max(answer, answers[i])
print(answer)

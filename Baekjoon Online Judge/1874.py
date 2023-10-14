import sys

input = sys.stdin.readline

answer = [''] * 200000
last = 0
stack = [0] * 100000
top = 0
n = int(input().rstrip())
seq = [0] * n
for i in range(n):
    seq[i] = int(input().rstrip())

num = 1
for i in range(n):
    if seq[i] >= num:
        while seq[i] >= num:
            stack[top] = num
            answer[last] = '+'
            top += 1
            num += 1
            last += 1
        answer[last] = '-'
        last += 1
        top -= 1
    else:
        if top == 0:
            print('NO')
            break
        elif seq[i] == stack[top - 1]:
            answer[last] = '-'
            last += 1
            top -= 1
        else:
            print('NO')
            break
if answer[2 * n - 1] != '':
    for i in range(2 * n):
        print(answer[i])

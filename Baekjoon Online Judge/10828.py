import sys

input = sys.stdin.readline

stack = [0] * 10000
top = 0

N = int(input().rstrip())
for _ in range(N):
    instruction = input().split()
    if instruction[0] == 'push':
        stack[top] = int(instruction[1])
        top += 1
    elif instruction[0] == 'pop':
        if top == 0:
            print(-1)
        else:
            print(stack[top - 1])
            top -= 1
    elif instruction[0] == 'size':
        print(top)
    elif instruction[0] == 'empty':
        if top == 0:
            print(1)
        else:
            print(0)
    else:
        if top == 0:
            print(-1)
        else:
            print(stack[top - 1])

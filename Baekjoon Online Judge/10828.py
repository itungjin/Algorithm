# 스택

import sys
from collections import deque
input = sys.stdin.readline

stack = deque()

N = int(input().rstrip())
for _ in range(N):
    instruction = input().rstrip()
    if len(instruction.split()) == 1:
        if instruction == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif instruction == "size":
            print(len(stack))
        elif instruction == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:  # instruction == "top"
            if len(stack) != 0:
                print(stack[len(stack) - 1])
            else:
                print(-1)
    else:  # instruction == "push"
        _, X = instruction.split()
        stack.append(int(X))

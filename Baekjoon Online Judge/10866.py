# 덱

import sys
input = sys.stdin.readline

MX = 10000
deque = [0 for _ in range(2*MX + 1)]
head, tail = MX, MX

N = int(input().rstrip())
for _ in range(N):
    instruction = input().rstrip()
    if len(instruction.split()) == 2:
        instruction, X = instruction.split()
        if instruction == "push_front":
            head -= 1
            deque[head] = X
        else:  # push_back
            deque[tail] = X
            tail += 1
    else:
        if instruction == 'pop_front':
            if head == tail:
                print(-1)
            else:
                print(deque[head])
                head += 1
        elif instruction == 'pop_back':
            if head == tail:
                print(-1)
            else:
                tail -= 1
                print(deque[tail])
        elif instruction == 'size':
            print(tail - head)
        elif instruction == 'empty':
            if head == tail:
                print(1)
            else:
                print(0)
        elif instruction == 'front':
            if head == tail:
                print(-1)
            else:
                print(deque[head])
        else:  # back
            if head == tail:
                print(-1)
            else:
                print(deque[tail - 1])

# 큐

import sys
input = sys.stdin.readline

queue = [0 for _ in range(2000001)]
head, tail = 0, 0
N = int(input().rstrip())

for _ in range(N):
    instruction = input().rstrip()
    if len(instruction.split()) == 2:
        _, X = instruction.split()
        queue[tail] = X
        tail += 1
    else:
        if instruction == 'pop':
            if head == tail:
                print(-1)
            else:
                print(queue[head])
                head += 1
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
                print(queue[head])
        else:  # back
            if head == tail:
                print(-1)
            else:
                print(queue[tail - 1])

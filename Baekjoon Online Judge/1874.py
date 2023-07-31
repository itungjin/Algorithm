# 스택

from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
pushable = 1
stack = deque()
answer = deque()
for _ in range(n):
    num = int(input().rstrip())
    if num < pushable:
        if len(stack) > 0 and stack.pop() == num:
            answer.append('-')
        else:
            answer.appendleft(False)
            break
    elif num == pushable:
        answer.append('+')
        answer.append('-')
        pushable += 1
    else:
        while pushable <= num:
            answer.append('+')
            stack.append(pushable)
            pushable += 1
        answer.append('-')
        stack.pop()
if answer[0] == False:
    print('NO')
else:
    for opr in answer:
        print(opr)

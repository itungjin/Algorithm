import sys
input = sys.stdin.readline

n = int(input().rstrip())
seq = [0] * n
for i in range(n):
    seq[i] = int(input().rstrip())

answer = []
stack = []
i = 1
is_possible = True
for element in seq:
    if element >= i:
        while element >= i:
            stack.append(i)
            answer.append('+')
            i += 1
        stack.pop()
        answer.append('-')
    else:
        a = stack.pop()
        answer.append('-')
        if a != element:
            is_possible = False
            break

if is_possible:
    for opr in answer:
        print(opr)
else:
    print('NO')
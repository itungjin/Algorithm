import sys

data = sys.stdin.readline().rstrip()
stack = []
answer = 0
prev_open = False
for char in data:
    if char == '(':
        stack.append(char)
        prev_open = True
        answer += 1
    else:
        if prev_open:
            prev_open = False
            answer += len(stack) - 2
        stack.pop()
print(answer)
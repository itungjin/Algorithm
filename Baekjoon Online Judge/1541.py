import sys

input = sys.stdin.readline
exp = input().rstrip()
stack = []
operator = True
for char in exp:
    if char.isdigit():
        if stack and type(stack[-1]) == int:
            stack.append(stack.pop() * 10 + int(char))
        else:
            stack.append(int(char))
    else:
        if not operator:
            stack.append('-')
        else:
            if char == '+':
                stack.append('+')
            else:
                operator = False
                stack.append('-')
answer = stack[0]
for i in range(2, len(stack), 2):
    if stack[i - 1] == '+':
        answer += stack[i]
    else:
        answer -= stack[i]
print(answer)

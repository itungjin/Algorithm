import sys
input = sys.stdin.readline

N = int(input().rstrip())
answer = 0
for _ in range(N):
    word = input().rstrip()
    stack = []
    for char in word:
        if char == 'A':
            if not stack or stack[-1] == 'B':
                stack.append(char)
            else:
                stack.pop()
        else:
            if not stack or stack[-1] == 'A':
                stack.append(char)
            else:
                stack.pop()
    if not stack:
        answer += 1

print(answer)
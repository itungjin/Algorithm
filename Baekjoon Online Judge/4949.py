import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break

    stack = []
    is_balanced = True
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack:
                is_balanced = False
                break
            else:
                if stack.pop() != '(':
                    is_balanced = False
                    break
        elif char == ']':
            if not stack:
                is_balanced = False
                break
            else:
                if stack.pop() != '[':
                    is_balanced = False
                    break
    if stack:
        is_balanced = False
    
    if is_balanced:
        print('yes')
    else:
        print('no')
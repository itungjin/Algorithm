string = input()
stack = []
is_right = True
for char in string:
    if char == '(' or char == '[':
        stack.append(char)
    elif char == ')':
        if not stack or stack.pop() != '(':
            is_right = False
            break
    else:
        if not stack or stack.pop() != '[':
            is_right = False
            break

if stack:
    is_right = False

if not is_right:
    print(0)
else:
    exp = list(string)
    while not all(type(char) == int for char in exp):
        string = exp[:]
        exp.clear()
        open_front = False
        mul = 1
        for i in range(len(string)):
            if string[i] == '(' or string[i] == '[':
                exp.append(string[i])
                open_front = True
                mul = 1
            elif string[i] == ')':
                if open_front:
                    if type(exp[-1]) == int:
                        exp.pop()
                    exp.pop()
                    temp = mul * 2
                    exp.append(temp)
                else:
                    exp.append(')')
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] == '['):
                    exp.append('+')
                open_front = False
            elif string[i] == ']':
                if open_front:
                    if type(exp[-1]) == int:
                        exp.pop()
                    exp.pop()
                    temp = mul * 3
                    exp.append(temp)
                else:
                    exp.append(']')
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] == '['):
                    exp.append('+')
                open_front = False
            elif string[i] == '+':
                exp.append(string[i])
            else: # 숫자
                mul *= string[i]
                exp.append(string[i])
        string = exp[:]
        exp.clear()
        for i in range(len(string)):
            if type(string[i]) != int:
                exp.append(string[i])
            else:
                if exp and exp[-1] == '+' and type(exp[-2]) == int and type(string[i]) == int:
                    exp.pop()
                    temp = exp.pop() + string[i]
                    exp.append(temp)
                else:
                    exp.append(string[i])
    print(exp[0])
            
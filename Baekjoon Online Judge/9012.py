import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    ps = input().rstrip()
    stack = []
    is_vps = True
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                is_vps = False
                break
            else:
                stack.pop()
    if stack:
        is_vps = False
    if is_vps:
        print('YES')
    else:
        print('NO')

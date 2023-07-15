# 구현

a, b, c = map(int, input().split())

if max(a, b, c) == a:
    if a < b + c:
        print(a + b + c)
    else:
        print(2 * (b + c) - 1)
elif max(a, b, c) == b:
    if b < a + c:
        print(a + b + c)
    else:
        print(2 * (a + c) - 1)
else:
    if c < a + b:
        print(a + b + c)
    else:
        print(2 * (a + b) - 1)

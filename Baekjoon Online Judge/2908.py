# 구현

A, B = input().split()

a, b = "", ""
for _a in A:
    a = _a + a
for _b in B:
    b = _b + b

print(max(int(a), int(b)))

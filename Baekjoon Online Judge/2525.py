# 구현

A, B = map(int, input().split())
C = int(input())

A += C // 60
B += C % 60
if B > 59:
    B -= 60
    A += 1
if A > 23:
    A %= 24

print(A, B)

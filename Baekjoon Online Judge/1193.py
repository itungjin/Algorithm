# 구현

X = int(input())

i = 1
while True:
    if X - i <= 0:
        i += 1
        break
    X -= i
    i += 1

if i % 2 == 0:
    print(str(i - X) + "/" + str(X))
else:
    print(str(X) + "/" + str(i - X))

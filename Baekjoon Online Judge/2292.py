# 구현

N = int(input())
N -= 1

if N == 0:
    print(1)
else:
    i = 0
    while True:
        if 3*i*(i+1) < N <= 3*(i+1)*(i+2):
            break
        i += 1

    print(i + 2)

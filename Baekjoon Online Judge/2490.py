# 구현

for _ in range(3):
    yuts = list(map(int, input().split()))

    bae = 0
    for yut in yuts:
        if yut == 0:
            bae += 1

    if bae == 4:
        print('D')
    elif bae == 3:
        print('C')
    elif bae == 2:
        print('B')
    elif bae == 1:
        print('A')
    else:
        print('E')

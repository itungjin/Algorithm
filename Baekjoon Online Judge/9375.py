import sys

input = sys.stdin.readline

test_case = int(input().rstrip())
for _ in range(test_case):
    n = int(input().rstrip())
    clothes = dict()
    for _ in range(n):
        _, type = input().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
    clothes = list(clothes.values())
    if len(clothes) == 1:
        print(clothes[0])
    else:
        ans = 1
        for cloth in clothes:
            ans *= (cloth + 1)
        ans -= 1
        print(ans)

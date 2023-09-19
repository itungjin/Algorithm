import sys

input = sys.stdin.readline

N = int(input().rstrip())
sns = [[] for _ in range(51)]
for _ in range(N):
    sn = input().rstrip()
    total = 0
    for char in sn:
        if char.isdigit():
            total += int(char)
    sns[len(sn)].append([total, sn])
for i in range(1, 51):
    sns[i].sort()
    for sn in sns[i]:
        print(sn[1])

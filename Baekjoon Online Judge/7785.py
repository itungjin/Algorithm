import sys

input = sys.stdin.readline

n = int(input().rstrip())
names = set()
for i in range(n):
    name, _ = input().split()
    if name not in names:
        names.add(name)
    else:
        names.remove(name)

names = list(names)
names.sort(reverse=True)
for name in names:
    print(name)

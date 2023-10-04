import sys

input = sys.stdin.readline

na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = [x for x in a if x not in b]
c.sort()
print(len(c))
print(*c)

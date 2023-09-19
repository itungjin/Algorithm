import sys
from operator import itemgetter

input = sys.stdin.readline

N = int(input().rstrip())
members = [0] * N
for i in range(N):
    age, name = input().split()
    age = int(age)
    members[i] = (age, name)
members.sort(key=itemgetter(0))
for member in members:
    print(*member)

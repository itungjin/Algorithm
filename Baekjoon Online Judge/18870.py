import sys

input = sys.stdin.readline

N = int(input().rstrip())
X = list(map(int, input().split()))
x2 = sorted(list(set(X)))
x3 = dict()
for i in range(len(x2)):
    x3[x2[i]] = i
for x in X:
    print(x3[x], end=' ')

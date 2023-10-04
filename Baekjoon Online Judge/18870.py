import sys
from bisect import bisect
input = sys.stdin.readline

N = int(input().rstrip())
X = list(map(int, input().split()))
x2 = sorted(X)
x3 = [x2[0]]
for i in range(1, len(x2)):
    if x2[i] != x2[i-1]:
        x3.append(x2[i])
for x in X:
    print(bisect(x3, x) - 1, end=' ')
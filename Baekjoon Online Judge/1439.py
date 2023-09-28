import sys

input = sys.stdin.readline

S = input().rstrip()
count = [0] * 2
count[int(S[0])] += 1
for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        count[int(S[i])] += 1
print(min(count))

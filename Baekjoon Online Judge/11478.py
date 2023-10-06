import sys

input = sys.stdin.readline

S = input().rstrip()
sub_string = set()
for length in range(1, len(S) + 1):
    for i in range(len(S) - length + 1):
        sub_string.add(S[i:i + length])
print(len(sub_string))

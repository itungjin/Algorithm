import sys

input = sys.stdin.readline

N = int(input().rstrip())
words = [0] * N
for i in range(N):
    word = input().rstrip()
    words[i] = [len(word), word]
words.sort()
print(words[0][1])
for i in range(1, N):
    if words[i][1] == words[i - 1][1]:
        continue
    print(words[i][1])

# 구현

S = input()

alphabets = [0] * 26
for alphabet in S:
    alphabets[ord(alphabet) - ord('a')] += 1

print(*alphabets)

# 구현

str1 = input()
str2 = input()

alphabets1 = [0] * 26
alphabets2 = [0] * 26
for char in str1:
    alphabets1[ord(char) - ord('a')] += 1
for char in str2:
    alphabets2[ord(char) - ord('a')] += 1

answer = 0
for i in range(26):
    answer += abs(alphabets1[i] - alphabets2[i])

print(answer)

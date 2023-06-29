# 구현

word = input()

answer = 0
for char in word:
    if (ord(char) < ord('S')):
        answer += ((ord(char) - 56) // 3)
    elif (ord(char) < ord('Z')):
        answer += ((ord(char) - 57) // 3)
    else:
        answer += ((ord(char) - 58) // 3)

print(answer)

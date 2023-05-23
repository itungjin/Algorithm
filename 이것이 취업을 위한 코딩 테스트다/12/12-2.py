# 구현
# S는 주어진 문자열
# 알파벳은 오름차순으로 정렬
# 숫자는 더해서 문자열로 변환

s = input()
answer = ""

alphabets = []
num = 0
for char in s:
    if char.isalpha():
        alphabets.append(char)
    else:
        num += int(char)
alphabets.sort()
answer = "".join(alphabets)
answer += str(num)

print(answer)

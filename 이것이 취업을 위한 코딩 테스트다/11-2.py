# 그리디
# S는 0부터 9의 숫자로 이루어진 문자열
# 더하기 또는 곱하기의 연산자를 S의 요소 사이에 넣을 수 있음
# 더하기, 곱하기 연산의 우선순위는 무시되고 왼쪽부터 연산

s = input()
answer = int(s[0])
for i in range(1, len(s)):
    answer = max(answer + int(s[i]), answer * int(s[i]))

print(answer)

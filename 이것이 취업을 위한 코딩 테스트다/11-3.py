# 그리디
# S는 0과 1로만 이루어진 문자열
# 연속된 1을 0으로 바꾸거나 연속된 0을 1로 바꾸어 문자열을 한 숫자로만 구성되게 변경
# 0과 1이 교차된 횟수를 비교하고 규칙을 찾음

s = input()
answer = 0

chr_now = s[0]
for i in range(1, len(s)):
    if (chr_now != s[i]):
        chr_now = s[i]
        answer += 1

print((answer + 1) // 2)

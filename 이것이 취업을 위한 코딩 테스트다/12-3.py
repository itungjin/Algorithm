# 구현
# s는 길이가 1 이상 1000 이하인 알파벳 소문자로 이루어진 문자열
# 1개 이상 s의 길이의 절반 이하로 단위를 바꿔가며 시도

def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        compressed_s = ""
        token = s[:i]
        count = 1
        for j in range(i, len(s), i):
            if token == s[j:j + i]:
                count += 1
            else:
                if count == 1:
                    compressed_s = compressed_s + token
                else:
                    compressed_s = compressed_s + token + str(count)
                    count = 1
                token = s[j:j + i]
        if count == 1:
            compressed_s = compressed_s + token
        else:
            compressed_s = compressed_s + token + str(count)
        answer = min(answer, len(compressed_s))

    return answer

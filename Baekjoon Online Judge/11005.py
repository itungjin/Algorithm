# 구현

N, B = map(int, input().split())

answer = ""
while N > 0:
    remainder = N % B
    N = N // B
    if remainder >= 10:
        remainder = chr(ord('A') + remainder - 10)
    else:
        remainder = str(remainder)
    answer = remainder + answer

print(answer)

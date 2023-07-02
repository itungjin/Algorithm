# 구현

import math

N, B = input().split()
B = int(B)

answer = 0
for i in range(len(N)):
    if N[i].isdigit():
        answer += int(N[i]) * int(math.pow(B, len(N) - i - 1))
    else:
        answer += (ord(N[i]) - ord('A') + 10) * \
            int(math.pow(B, len(N) - i - 1))

print(answer)

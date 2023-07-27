# 구현

import sys
input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N):
    str1, str2 = input().split()

    alphabets = [0] * 26
    for char in str1:
        alphabets[ord(char) - ord('a')] += 1
    for char in str2:
        alphabets[ord(char) - ord('a')] -= 1

    possible = True
    for alphabet in alphabets:
        if alphabet != 0:
            possible = False
            break
    if possible:
        print('Possible')
    else:
        print('Impossible')

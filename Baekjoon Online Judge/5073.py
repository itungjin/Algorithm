# 구현

import sys
input = sys.stdin.readline

while True:
    s1, s2, s3 = map(int, input().split())
    if s1 == s2 == s3 == 0:
        break

    if max(s1, s2, s3) == s1 and s1 >= s2 + s3 or max(s1, s2, s3) == s2 and s2 >= s1 + s3 or max(s1, s2, s3) == s3 and s3 >= s1 + s2:
        print('Invalid')
    else:
        if s1 == s2 == s3:
            print('Equilateral')
        elif s1 != s2 and s2 != s3 and s1 != s3:
            print('Scalene')
        else:
            print('Isosceles')

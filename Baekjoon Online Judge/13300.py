# 구현

import sys

input = sys.stdin.readline

students = [[0] * 7, [0] * 7]

N, K = map(int, input().split())
for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1

answer = 0
for student in students[0]:
    answer += (student + (K-1)) // K
for student in students[1]:
    answer += (student + (K-1)) // K

print(answer)

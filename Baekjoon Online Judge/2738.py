# 구현

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = [[] for _ in range(N)]
B = [[] for _ in range(N)]
sum_matrix = [[0] * M for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))
for i in range(N):
    B[i] = list(map(int, input().split()))
    for j in range(M):
        sum_matrix[i][j] = A[i][j] + B[i][j]

for i in range(N):
    for j in range(M):
        print(sum_matrix[i][j], end=' ')
    print()

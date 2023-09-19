import sys
from operator import itemgetter

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N, M = map(int, input().split())
    creatures = [0] * (N + M)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(N):
        creatures[i] = [A[i], 0]
    for i in range(M):
        creatures[N + i] = [B[i], 1]
    creatures.sort(key=itemgetter(0))
    count = 0
    answer = 0
    for i in range(N + M):
        if creatures[i][1] == 0:
            answer += i - count
            count += 1
    print(answer)

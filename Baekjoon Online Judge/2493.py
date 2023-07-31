from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
towers = list(map(int, input().split()))

answer = [0 for _ in range(N)]


def find(start, end):
    if end < 0:
        return 0
    else:
        if towers[start] <= towers[end]:
            return end + 1
        else:
            return find(start, answer[end] - 1)


for i in range(1, N):
    answer[i] = find(i, i-1)

print(*answer)

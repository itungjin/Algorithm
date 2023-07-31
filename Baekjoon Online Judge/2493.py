from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
towers = list(map(int, input().split()))
stack = deque()
answers = [0 for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if towers[j] > towers[i]:
            break
        else:
            answers[j] = i+1

print(*answers)

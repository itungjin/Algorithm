import sys
input = sys.stdin.readline

N = int(input().rstrip())
heights = [0] * (N)
for i in range(N):
    heights[i] = int(input().rstrip())
answer = 0

import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input().rstrip()))

answer = 0
while len(cards) != 1:
    comparison = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, comparison)
    answer += comparison

print(answer)

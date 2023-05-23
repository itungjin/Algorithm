import sys
import heapq

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline().rstrip()))

answer = 0
while len(cards) > 1:
    first, second = heapq.heappop(cards), heapq.heappop(cards)
    answer += first + second
    heapq.heappush(cards, first + second)

print(answer)

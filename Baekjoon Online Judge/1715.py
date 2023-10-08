import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
cards = [int(input().rstrip()) for _ in range(N)]
answer = 0
heapq.heapify(cards)
while len(cards) != 1:
    a, b = heapq.heappop(cards), heapq.heappop(cards)
    heapq.heappush(cards, a + b)
    answer += a + b
print(answer)
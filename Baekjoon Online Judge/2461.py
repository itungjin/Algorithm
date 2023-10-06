import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
ability = [list(map(int, input().split())) for _ in range(N)]
pointer = [0] * N
top = 0
bottom = []
for i in range(N):
    ability[i].sort()
    if ability[i][0] > top:
        top = ability[i][0]
    heapq.heappush(bottom, (ability[i][0], i))
answer = top - bottom[0][0]
while True:
    pointer[bottom[0][1]] += 1
    if pointer[bottom[0][1]] == M:
        break
    if ability[bottom[0][1]][pointer[bottom[0][1]]] > top:
        top = ability[bottom[0][1]][pointer[bottom[0][1]]]
    heapq.heappush(bottom, (ability[bottom[0][1]][pointer[bottom[0][1]]], bottom[0][1]))
    heapq.heappop(bottom)
    answer = min(answer, top - bottom[0][0])
print(answer)
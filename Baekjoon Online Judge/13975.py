import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    K = int(input().rstrip())
    files = list(map(int, input().split()))
    heapq.heapify(files)

    answer = 0
    while len(files) != 1:
        temp_file = heapq.heappop(files) + heapq.heappop(files)
        heapq.heappush(files, temp_file)
        answer += temp_file

    print(answer)

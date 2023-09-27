import sys

input = sys.stdin.readline

N = int(input().rstrip())
ropes = [int(input().rstrip()) for _ in range(N)]
ropes.sort(reverse=True)
answer = 0
weak = 0
count = 0
for rope in ropes:
    count += 1
    if rope * count >= answer:
        answer = rope * count
print(answer)

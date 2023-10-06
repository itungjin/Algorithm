import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input().rstrip()) for _ in range(N)]
for i in range(k - 1):
    belt.append(belt[i])
sushi = [0] * 3001
answer = 0
count = 0
end = -1
for start in range(N):
    while end - start != k - 1:
        end += 1
        if not sushi[belt[end]]:
            count += 1
        sushi[belt[end]] += 1
    if not sushi[c]:
        answer = max(answer, count + 1)
    else:
        answer = max(answer, count)
    sushi[belt[start]] -= 1
    if not sushi[belt[start]]:
        count -= 1
print(answer)

# 구현

import sys
input = sys.stdin.readline

paper = [[True] * 100 for _ in range(100)]
answer = 0
for _ in range(int(input().rstrip())):
    x, y = map(int, input().split())
    for c in range(x, x + 10):
        for r in range(y, y + 10):
            if paper[r][c]:
                paper[r][c] = False
                answer += 1

print(answer)

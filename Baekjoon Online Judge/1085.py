# 구현

x, y, w, h = map(int, input().split())

answer = 1000

answer = min(answer, x)
answer = min(answer, y)
answer = min(answer, w - x)
answer = min(answer, h - y)

print(answer)

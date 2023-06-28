# 완전 탐색

N = int(input())
integers = list(map(int, input().split()))
v = int(input())

answer = 0
for integer in integers:
    if integer == v:
        answer += 1

print(answer)

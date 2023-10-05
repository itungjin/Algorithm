import sys

input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))
left = 0
right = 0

answer = 100001
subtotal = seq[0]
while right < N:
    if subtotal >= S:
        answer = min(answer, right - left + 1)
        subtotal -= seq[left]
        left += 1
    else:
        right += 1
        if right == N:
            break
        subtotal += seq[right]


if answer == 100001:
    print(0)
else:
    print(answer)

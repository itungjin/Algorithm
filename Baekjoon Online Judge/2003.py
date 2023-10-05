import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
answer = 0
left = 0
right = -1
subtotal = 0

while True:
    if subtotal < M:
        right += 1
        if right == N:
            break
        subtotal += A[right]
    elif subtotal == M:
        answer += 1
        right += 1
        if right == N:
            break
        subtotal += A[right] - A[left]
        left += 1
    else:
        subtotal -= A[left]
        left += 1
print(answer)

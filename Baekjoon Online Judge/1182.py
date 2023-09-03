N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
count = 0


def solution(n, _sum, is_new):
    global count
    count += 1
    if is_new and _sum == S:
        global answer
        answer += 1

    if n == N:
        return

    solution(n + 1, _sum, False)
    solution(n + 1, _sum + arr[n], True)


solution(0, 0, False)
print(answer)
print(count)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = [0] * M


def solution(n):
    if n == M:
        print(*answer)
        return

    for i in range(1, N + 1):
        answer[n] = arr[i - 1]
        solution(n + 1)


solution(0)
